import streamlit as st
from pycoingecko import CoinGeckoAPI
from web3 import Web3
import torch
import torch.nn as nn
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from dotenv import load_dotenv
import os
import time
import requests
import json
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

load_dotenv()
VENICE_API_KEY = os.getenv('VENICE_API_KEY')

class BlockchainService:
    """
    Service for blockchain queries with failover.
    """
    def __init__(self):
        try:
            self.w3 = Web3(Web3.HTTPProvider(os.getenv('ETHEREUM_RPC_URL')))
            self.fallback_w3 = Web3(Web3.HTTPProvider(os.getenv('ETHEREUM_FALLBACK_RPC_URL')))
        except Exception as e:
            logger.error(f"Failed to initialize Web3 providers: {e}")
            st.error("Blockchain providers not configured. Surveillance features disabled.")
            self.w3 = None
            self.fallback_w3 = None

    def get_large_transfers(self, token_address, blocks=100, min_amount=1000000, decimals=18):
        if not self.w3:
            return 0
        try:
            provider = self.w3 if self.w3.is_connected() else self.fallback_w3
            if not provider.is_connected():
                raise ConnectionError("No active provider")
            checksum_address = provider.to_checksum_address(token_address)
            logs = provider.eth.get_logs({
                'fromBlock': provider.eth.block_number - blocks,
                'toBlock': 'latest',
                'address': checksum_address,
                'topics': [['0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef']]
            })
            large = 0
            for log in logs:
                amount_hex = log['data']
                amount = int(amount_hex, 16) / (10 ** decimals)
                if amount > min_amount:
                    large += 1
            return large
        except (ConnectionError, ValueError, KeyError) as e:
            logger.warning(f"Blockchain query error: {e}. Returning 0.")
            st.warning(f"Blockchain query failed for {token_address}. Using default value.")
            return 0
        except Exception as e:
            logger.error(f"Unexpected blockchain error: {e}")
            return 0

class LSTM(nn.Module):
    """
    LSTM model for price prediction.
    """
    def __init__(self, input_size=3, hidden_layer_size=100, output_size=1):
        super().__init__()
        self.hidden_layer_size = hidden_layer_size
        self.lstm = nn.LSTM(input_size, hidden_layer_size, batch_first=True)
        self.linear = nn.Linear(hidden_layer_size, output_size)

    def forward(self, input_seq):
        batch_size = input_seq.size(0)
        h0 = torch.zeros(1, batch_size, self.hidden_layer_size).to(input_seq.device)
        c0 = torch.zeros(1, batch_size, self.hidden_layer_size).to(input_seq.device)
        lstm_out, _ = self.lstm(input_seq, (h0, c0))
        predictions = self.linear(lstm_out[:, -1, :])
        return predictions

def get_ai_recommendation(coin, growth, large_tx, current, predicted):
    """
    Get recommendation from Venice AI.
    """
    if not VENICE_API_KEY:
        return "Venice AI API key not configured."
    
    prompt = f"As a CIA DeFi surveillance agent, provide an uncensored analysis and automated strategy recommendation for {coin}. Predicted growth: {growth:.2f}%. Recent large transfers: {large_tx}. Current price: ${current:.2f}. Predicted price: ${predicted:.2f}. Include potential risks, DeFi maneuvers (e.g., staking, looping), and decision: buy, hold, or sell."
    
    headers = {
        "Authorization": f"Bearer {VENICE_API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "dolphin-72b",
        "messages": [{"role": "user", "content": prompt}]
    }
    
    try:
        response = requests.post("https://api.venice.ai/api/v1/chat/completions", headers=headers, json=data, timeout=10)
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.RequestException as e:
        logger.error(f"Venice AI request failed: {e}")
        return f"Venice AI error: {str(e)}"
    except KeyError:
        return "Invalid response from Venice AI."

@st.cache_data(ttl=7200)  # Cache for 2 hours
def predict_growth(coin_id, token_address=None):
    """
    Predict growth using market data and surveillance.
    """
    cg = CoinGeckoAPI()
    try:
        data = cg.get_coin_market_chart_by_id(id=coin_id, vs_currency='usd', days=60)
        if not data.get('prices') or not data.get('total_volumes'):
            raise ValueError("Incomplete market data")
    except Exception as e:
        logger.error(f"CoinGecko API error for {coin_id}: {e}")
        st.error(f"CoinGecko API error for {coin_id}. Skipping.")
        return 0.0, 0, 0.0, 0.0

    prices = pd.DataFrame(data['prices'], columns=['time', 'price'])
    volumes = pd.DataFrame(data['total_volumes'], columns=['time', 'volume'])
    df = prices.merge(volumes, on='time')

    large_transfers = 0
    if token_address:
        bs = BlockchainService()
        large_transfers = bs.get_large_transfers(token_address)

    df['large_tx'] = large_transfers

    scaler = MinMaxScaler(feature_range=(-1, 1))
    scaled_data = scaler.fit_transform(df[['price', 'volume', 'large_tx']])

    look_back = 30
    if len(scaled_data) < look_back + 1:
        logger.warning(f"Insufficient data for {coin_id}. Returning default.")
        current_price = df['price'].iloc[-1] if not df.empty else 0.0
        return 0.0, large_transfers, current_price, 0.0

    x, y = [], []
    for i in range(look_back, len(scaled_data)):
        x.append(scaled_data[i - look_back:i])
        y.append(scaled_data[i, 0])

    x = np.array(x)
    y = np.array(y)
    x = torch.from_numpy(x).type(torch.Tensor)
    y = torch.from_numpy(y).type(torch.Tensor)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    logger.info(f"Using device: {device}")

    current_price = df['price'].iloc[-1]

    try:
        model = LSTM(input_size=3).to(device)
        loss_function = nn.MSELoss()
        optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
        epochs = 50
        x, y = x.to(device), y.to(device)

        for i in range(epochs):
            optimizer.zero_grad()
            y_pred = model(x)
            single_loss = loss_function(y_pred.squeeze(), y)
            single_loss.backward()
            optimizer.step()

        # Predict next day
        test_inputs = scaled_data[-look_back:].tolist()
        num_predictions = 1  # Next day
        for _ in range(num_predictions):
            seq = torch.FloatTensor(test_inputs[-look_back:]).unsqueeze(0).to(device)
            with torch.no_grad():
                next_pred = model(seq).item()
                test_inputs.append([next_pred, test_inputs[-1][1], test_inputs[-1][2]])  # Append predicted price, last volume/tx

        # Inverse transform to get actual predicted price
        predicted_scaled = np.array(test_inputs[look_back:])[:, 0].reshape(-1, 1)
        dummy = np.zeros((len(predicted_scaled), 3))  # To inverse with full features
        dummy[:, 0] = predicted_scaled[:, 0]
        predicted_price = scaler.inverse_transform(dummy)[0][0]

        growth = (predicted_price - current_price) / current_price * 100

        # Agentic adjustment: Boost growth score if high surveillance activity
        if large_transfers > 5:  # Arbitrary threshold for "high activity"
            growth += 2.0  # Add bonus for potential whale momentum

        return growth, large_transfers, current_price, predicted_price
    except RuntimeError as e:
        logger.error(f"PyTorch runtime error for {coin_id}: {e}")
        st.error(f"Model training failed for {coin_id}. Using defaults.")
        return 0.0, large_transfers, current_price, current_price

# Dashboard UI
st.title("CIA-Style DeFi Surveillance & Prediction Dashboard")
st.markdown("Combines on-chain forensics with AI-driven predictions. Enhanced error handling and optimization.")

cryptos = {
    'bitcoin': None,
    'ethereum': None,
    'tether': '0xdac17f958d2ee523a2206206994597c13d831ec7',
    'solana': None,
    'binancecoin': '0xb8c77482e45f1f44de1745f52c74426c631bdd52'
}

results = []
for coin_id, token_addr in cryptos.items():
    with st.spinner(f"Analyzing {coin_id.capitalize()}..."):
        try:
            growth, large_tx, current, predicted = predict_growth(coin_id, token_addr)
            results.append((coin_id, growth, large_tx, current, predicted))
        except Exception as e:
            logger.error(f"Analysis failed for {coin_id}: {e}")
            st.warning(f"Skipping {coin_id} due to error.")
        time.sleep(0.5)  # Reduced delay

if results:
    results.sort(key=lambda x: x[1], reverse=True)
    df_results = pd.DataFrame(results, columns=['Crypto', 'Predicted Growth (%)', 'Large Transfers (Recent)', 'Current Price ($)', 'Predicted Price ($)'])
    st.subheader("Ranked Predictions")
    st.dataframe(df_results.style.format({'Predicted Growth (%)': '{:.2f}', 'Current Price ($)': '{:.2f}', 'Predicted Price ($)': '{:.2f}'}))

    st.subheader("AI-Agentic Recommendations (Powered by Venice AI)")
    for coin, growth, large_tx, current, predicted in results:
        with st.expander(f"Recommendation for {coin.capitalize()}"):
            rec = get_ai_recommendation(coin, growth, large_tx, current, predicted)
            st.markdown(rec)
else:
    st.error("No data available. Check API keys and connections.")
