# crypto-sentinel-dashboard
Enterprise-grade blockchain forensics &amp; AI intelligence platform
html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Crypto Sentinel Dashboard | Ernest Kofi Antwi</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary: #2563eb;
            --primary-dark: #1d4ed8;
            --secondary: #7c3aed;
            --dark: #0f172a;
            --dark-light: #1e293b;
            --light: #f8fafc;
            --accent: #06d6a0;
            --warning: #f59e0b;
            --danger: #ef4444;
            --border: #334155;
            --shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3);
            --radius: 12px;
            --transition: all 0.3s ease;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
            color: var(--light);
            line-height: 1.6;
            padding: 0;
            margin: 0;
            min-height: 100vh;
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        /* Header Styles */
        .header {
            background: linear-gradient(90deg, var(--dark) 0%, var(--dark-light) 100%);
            border-bottom: 1px solid var(--border);
            padding: 30px 0;
            position: relative;
            overflow: hidden;
        }
        
        .header::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: radial-gradient(circle at 20% 50%, rgba(37, 99, 235, 0.1) 0%, transparent 50%),
                        radial-gradient(circle at 80% 20%, rgba(124, 58, 237, 0.1) 0%, transparent 50%);
        }
        
        .project-title {
            font-size: 3rem;
            font-weight: 800;
            background: linear-gradient(90deg, var(--accent) 0%, var(--primary) 50%, var(--secondary) 100%);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            margin-bottom: 10px;
        }
        
        .project-subtitle {
            font-size: 1.2rem;
            color: #cbd5e1;
            max-width: 800px;
            margin-bottom: 30px;
        }
        
        .author-badge {
            display: inline-flex;
            align-items: center;
            background: rgba(30, 41, 59, 0.8);
            padding: 8px 16px;
            border-radius: 50px;
            border: 1px solid var(--border);
            margin-top: 10px;
        }
        
        .author-badge img {
            width: 32px;
            height: 32px;
            border-radius: 50%;
            margin-right: 10px;
            border: 2px solid var(--accent);
        }
        
        /* Badge Styles */
        .badge {
            display: inline-block;
            padding: 6px 12px;
            border-radius: 6px;
            font-size: 0.85rem;
            font-weight: 600;
            margin: 0 5px 10px 0;
        }
        
        .badge-primary {
            background: rgba(37, 99, 235, 0.2);
            color: #60a5fa;
            border: 1px solid rgba(37, 99, 235, 0.4);
        }
        
        .badge-secondary {
            background: rgba(124, 58, 237, 0.2);
            color: #a78bfa;
            border: 1px solid rgba(124, 58, 237, 0.4);
        }
        
        .badge-success {
            background: rgba(6, 214, 160, 0.2);
            color: var(--accent);
            border: 1px solid rgba(6, 214, 160, 0.4);
        }
        
        .badge-warning {
            background: rgba(245, 158, 11, 0.2);
            color: #fbbf24;
            border: 1px solid rgba(245, 158, 11, 0.4);
        }
        
        /* Card Styles */
        .card {
            background: var(--dark-light);
            border-radius: var(--radius);
            padding: 25px;
            margin-bottom: 25px;
            border: 1px solid var(--border);
            box-shadow: var(--shadow);
            transition: var(--transition);
        }
        
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.3);
        }
        
        .card-header {
            display: flex;
            align-items: center;
            margin-bottom: 20px;
            padding-bottom: 15px;
            border-bottom: 1px solid var(--border);
        }
        
        .card-icon {
            width: 50px;
            height: 50px;
            background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%);
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-right: 15px;
            font-size: 1.5rem;
        }
        
        .card-title {
            font-size: 1.5rem;
            font-weight: 700;
        }
        
        /* Feature Grid */
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 20px;
            margin: 30px 0;
        }
        
        .feature-item {
            background: rgba(30, 41, 59, 0.6);
            border-radius: 10px;
            padding: 20px;
            border-left: 4px solid var(--primary);
            transition: var(--transition);
        }
        
        .feature-item:hover {
            background: rgba(30, 41, 59, 0.8);
            transform: translateX(5px);
        }
        
        .feature-icon {
            color: var(--accent);
            font-size: 1.5rem;
            margin-bottom: 10px;
        }
        
        /* Tech Stack */
        .tech-stack {
            display: flex;
            flex-wrap: wrap;
            gap: 10px;
            margin: 15px 0;
        }
        
        .tech-item {
            background: rgba(15, 23, 42, 0.8);
            padding: 8px 15px;
            border-radius: 20px;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.9rem;
            border: 1px solid var(--border);
            transition: var(--transition);
        }
        
        .tech-item:hover {
            background: rgba(37, 99, 235, 0.2);
            border-color: var(--primary);
        }
        
        /* Button Styles */
        .btn {
            display: inline-flex;
            align-items: center;
            padding: 12px 24px;
            border-radius: 8px;
            font-weight: 600;
            text-decoration: none;
            transition: var(--transition);
            margin: 5px;
        }
        
        .btn-primary {
            background: linear-gradient(90deg, var(--primary) 0%, var(--primary-dark) 100%);
            color: white;
        }
        
        .btn-primary:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(37, 99, 235, 0.3);
        }
        
        .btn-secondary {
            background: rgba(30, 41, 59, 0.8);
            color: white;
            border: 1px solid var(--border);
        }
        
        .btn-secondary:hover {
            background: rgba(30, 41, 59, 1);
            border-color: var(--primary);
        }
        
        .btn-icon {
            margin-right: 8px;
        }
        
        /* Code Block */
        .code-block {
            background: rgba(15, 23, 42, 0.9);
            border-radius: 10px;
            padding: 20px;
            margin: 20px 0;
            border: 1px solid var(--border);
            overflow-x: auto;
            font-family: 'JetBrains Mono', monospace;
            font-size: 0.95rem;
        }
        
        .code-line {
            padding: 5px 0;
        }
        
        .code-comment {
            color: #64748b;
        }
        
        .code-keyword {
            color: #f472b6;
        }
        
        .code-function {
            color: #60a5fa;
        }
        
        .code-string {
            color: #34d399;
        }
        
        /* Timeline */
        .timeline {
            position: relative;
            padding-left: 30px;
            margin: 30px 0;
        }
        
        .timeline::before {
            content: '';
            position: absolute;
            left: 0;
            top: 0;
            bottom: 0;
            width: 2px;
            background: linear-gradient(to bottom, var(--primary), var(--secondary));
        }
        
        .timeline-item {
            position: relative;
            margin-bottom: 30px;
            padding-left: 20px;
        }
        
        .timeline-item::before {
            content: '';
            position: absolute;
            left: -36px;
            top: 5px;
            width: 12px;
            height: 12px;
            border-radius: 50%;
            background: var(--accent);
            border: 3px solid var(--dark);
        }
        
        .timeline-date {
            color: var(--accent);
            font-weight: 600;
            margin-bottom: 5px;
        }
        
        /* Footer */
        .footer {
            background: var(--dark);
            border-top: 1px solid var(--border);
            padding: 40px 0;
            margin-top: 60px;
            text-align: center;
        }
        
        .social-links {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin: 20px 0;
        }
        
        .social-link {
            width: 45px;
            height: 45px;
            border-radius: 50%;
            background: var(--dark-light);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 1.2rem;
            transition: var(--transition);
        }
        
        .social-link:hover {
            transform: translateY(-5px);
            background: var(--primary);
        }
        
        /* Responsive */
        @media (max-width: 768px) {
            .project-title {
                font-size: 2.2rem;
            }
            
            .feature-grid {
                grid-template-columns: 1fr;
            }
            
            .tech-stack {
                justify-content: center;
            }
        }
    </style>
</head>
<body>
    <!-- Header Section -->
    <header class="header">
        <div class="container">
            <div class="badge badge-primary">Enterprise-Grade Intelligence Platform</div>
            <h1 class="project-title">🛡️ Crypto Sentinel Dashboard</h1>
            <p class="project-subtitle">A production-grade blockchain forensics & AI intelligence platform combining on-chain surveillance, LSTM neural networks, and agentic AI for actionable financial intelligence. Built with Python, Streamlit, and enterprise security architecture.</p>
            
            <div class="author-badge">
                <div class="badge badge-success">By Ernest Kofi Antwi</div>
                <span style="margin: 0 10px">•</span>
                <span>Senior Software Engineer | 15+ Years Experience</span>
            </div>
            
            <div style="margin-top: 30px;">
                <a href="#demo" class="btn btn-primary">
                    <i class="fas fa-play btn-icon"></i> Live Demo
                </a>
                <a href="#installation" class="btn btn-secondary">
                    <i class="fas fa-download btn-icon"></i> Get Started
                </a>
                <a href="https://github.com/ErnestAntwi" class="btn btn-secondary">
                    <i class="fab fa-github btn-icon"></i> View on GitHub
                </a>
            </div>
        </div>
    </header>

    <!-- Main Content -->
    <main class="container" style="padding-top: 40px; padding-bottom: 40px;">
        
        <!-- Features Section -->
        <section id="features" class="card">
            <div class="card-header">
                <div class="card-icon">
                    <i class="fas fa-star"></i>
                </div>
                <h2 class="card-title">Core Intelligence Features</h2>
            </div>
            
            <div class="feature-grid">
                <div class="feature-item">
                    <div class="feature-icon">
                        <i class="fas fa-link"></i>
                    </div>
                    <h3>Blockchain Surveillance</h3>
                    <p>Real-time on-chain forensics monitoring ERC-20 contracts for large-value transfers (>$1M) with multi-provider failover.</p>
                </div>
                
                <div class="feature-item">
                    <div class="feature-icon">
                        <i class="fas fa-brain"></i>
                    </div>
                    <h3>AI Predictive Analytics</h3>
                    <p>LSTM neural networks trained on 60-day price/volume data enhanced with on-chain surveillance metrics.</p>
                </div>
                
                <div class="feature-item">
                    <div class="feature-icon">
                        <i class="fas fa-robot"></i>
                    </div>
                    <h3>Agentic Intelligence</h3>
                    <p>Venice AI integration for uncensored strategy analysis with automated buy/hold/sell recommendations.</p>
                </div>
                
                <div class="feature-item">
                    <div class="feature-icon">
                        <i class="fas fa-shield-alt"></i>
                    </div>
                    <h3>Enterprise Security</h3>
                    <p>Ready for SCIF deployment with Cisco Subnet isolation, Palo Alto NGFW, and Splunk SIEM integration.</p>
                </div>
            </div>
        </section>
        
        <!-- Tech Stack Section -->
        <section id="tech" class="card">
            <div class="card-header">
                <div class="card-icon">
                    <i class="fas fa-layer-group"></i>
                </div>
                <h2 class="card-title">Technology Stack</h2>
            </div>
            
            <div style="margin-bottom: 20px;">
                <h3 style="margin-bottom: 15px; color: var(--accent);">Core Framework</h3>
                <div class="tech-stack">
                    <span class="tech-item">Python 3.9+</span>
                    <span class="tech-item">Streamlit</span>
                    <span class="tech-item">PyTorch</span>
                    <span class="tech-item">Scikit-learn</span>
                </div>
            </div>
            
            <div style="margin-bottom: 20px;">
                <h3 style="margin-bottom: 15px; color: var(--accent);">Blockchain & APIs</h3>
                <div class="tech-stack">
                    <span class="tech-item">web3.py</span>
                    <span class="tech-item">Alchemy SDK</span>
                    <span class="tech-item">Infura API</span>
                    <span class="tech-item">CoinGecko API</span>
                    <span class="tech-item">Venice AI API</span>
                </div>
            </div>
            
            <div>
                <h3 style="margin-bottom: 15px; color: var(--accent);">Infrastructure & Security</h3>
                <div class="tech-stack">
                    <span class="tech-item">Docker</span>
                    <span class="tech-item">Cisco Subnet</span>
                    <span class="tech-item">Palo Alto NGFW</span>
                    <span class="tech-item">Splunk SIEM</span>
                    <span class="tech-item">Zero-Trust Architecture</span>
                </div>
            </div>
        </section>
        
        <!-- Quick Start Section -->
        <section id="installation" class="card">
            <div class="card-header">
                <div class="card-icon">
                    <i class="fas fa-rocket"></i>
                </div>
                <h2 class="card-title">Quick Start Installation</h2>
            </div>
            
            <h3 style="margin: 20px 0 15px 0; color: var(--accent);">1. Clone & Setup Environment</h3>
            <div class="code-block">
                <div class="code-line"><span class="code-comment"># Clone repository</span></div>
                <div class="code-line"><span class="code-function">git clone</span> https://github.com/ErnestAntwi/crypto-sentinel-dashboard.git</div>
                <div class="code-line"><span class="code-function">cd</span> crypto-sentinel-dashboard</div>
                <div class="code-line">&nbsp;</div>
                <div class="code-line"><span class="code-comment"># Create virtual environment</span></div>
                <div class="code-line">python -m venv venv</div>
                <div class="code-line"><span class="code-comment"># Activate (Windows)</span></div>
                <div class="code-line">venv<span class="code-keyword">\Scripts</span><span class="code-keyword">\activate</span></div>
                <div class="code-line"><span class="code-comment"># Activate (Mac/Linux)</span></div>
                <div class="code-line"><span class="code-function">source</span> venv<span class="code-keyword">/bin</span><span class="code-keyword">/activate</span></div>
            </div>
            
            <h3 style="margin: 25px 0 15px 0; color: var(--accent);">2. Configure Environment Variables</h3>
            <div class="code-block">
                <div class="code-line"><span class="code-comment"># Create .env file with your API keys</span></div>
                <div class="code-line"><span class="code-keyword">ETHEREUM_RPC_URL</span>=<span class="code-string">https://eth-mainnet.g.alchemy.com/v2/YOUR_KEY</span></div>
                <div class="code-line"><span class="code-keyword">ETHEREUM_FALLBACK_RPC_URL</span>=<span class="code-string">https://mainnet.infura.io/v3/YOUR_KEY</span></div>
                <div class="code-line"><span class="code-keyword">VENICE_API_KEY</span>=<span class="code-string">your_venice_ai_key</span></div>
            </div>
            
            <h3 style="margin: 25px 0 15px 0; color: var(--accent);">3. Install Dependencies & Run</h3>
            <div class="code-block">
                <div class="code-line"><span class="code-comment"># Install requirements</span></div>
                <div class="code-line">pip install -r requirements.txt</div>
                <div class="code-line">&nbsp;</div>
                <div class="code-line"><span class="code-comment"># Launch dashboard</span></div>
                <div class="code-line">streamlit run app/main.py</div>
                <div class="code-line">&nbsp;</div>
                <div class="code-line"><span class="code-comment"># Access at: http://localhost:8501</span></div>
            </div>
        </section>
        
        <!-- Architecture Section -->
        <section id="architecture" class="card">
            <div class="card-header">
                <div class="card-icon">
                    <i class="fas fa-sitemap"></i>
                </div>
                <h2 class="card-title">System Architecture</h2>
            </div>
            
            <div style="background: rgba(15, 23, 42, 0.7); padding: 20px; border-radius: 10px; margin: 20px 0;">
                <div style="text-align: center; padding: 10px; background: rgba(37, 99, 235, 0.1); border-radius: 8px; margin-bottom: 20px;">
                    <strong>Streamlit UI Layer</strong> ← Interactive Dashboard & Controls
                </div>
                
                <div style="text-align: center; padding: 10px; background: rgba(124, 58, 237, 0.1); border-radius: 8px; margin-bottom: 20px;">
                    <strong>AI Synthesis (Venice API)</strong> ← Strategy Recommendations & Risk Analysis
                </div>
                
                <div style="text-align: center; padding: 10px; background: rgba(6, 214, 160, 0.1); border-radius: 8px; margin-bottom: 20px;">
                    <strong>Predictive Engine (LSTM Neural Network)</strong> ← Price Forecasting & Pattern Recognition
                </div>
                
                <div style="text-align: center; padding: 10px; background: rgba(245, 158, 11, 0.1); border-radius: 8px; margin-bottom: 20px;">
                    <strong>Surveillance Layer (BlockchainService)</strong> ← On-Chain Transaction Monitoring
                </div>
                
                <div style="text-align: center; padding: 10px; background: rgba(30, 41, 59, 0.8); border-radius: 8px;">
                    <strong>Data Sources</strong> ← CoinGecko, Alchemy/Infura, On-chain Logs
                </div>
            </div>
            
            <div style="margin-top: 25px;">
                <h3 style="color: var(--accent); margin-bottom: 15px;">Key Design Patterns</h3>
                <ul style="padding-left: 20px; line-height: 1.8;">
                    <li><strong>Service Abstraction</strong>: Clean interfaces for component replacement/upgrade</li>
                    <li><strong>Failover Resilience</strong>: Automatic RPC provider switching</li>
                    <li><strong>Cached Computation</strong>: Memoization of expensive API calls</li>
                    <li><strong>Extensible Architecture</strong>: Plugin system for additional blockchains</li>
                </ul>
            </div>
        </section>
        
        <!-- Use Cases Section -->
        <section id="usecases" class="card">
            <div class="card-header">
                <div class="card-icon">
                    <i class="fas fa-briefcase"></i>
                </div>
                <h2 class="card-title">Intelligence Use Cases</h2>
            </div>
            
            <div class="feature-grid">
                <div class="feature-item" style="border-left-color: var(--danger);">
                    <h3>Financial Intelligence</h3>
                    <p>• Illicit flow detection & sanctions evasion tracking<br>• Market manipulation monitoring<br>• Institutional capital movement analysis</p>
                </div>
                
                <div class="feature-item" style="border-left-color: var(--warning);">
                    <h3>Investment Intelligence</h3>
                    <p>• Data-driven decision support systems<br>• Quantitative risk assessment frameworks<br>• Portfolio strategy automation</p>
                </div>
                
                <div class="feature-item" style="border-left-color: var(--accent);">
                    <h3>Security Operations</h3>
                    <p>• Blockchain threat intelligence platform<br>• Incident response tooling<br>• Regulatory compliance monitoring</p>
                </div>
            </div>
        </section>
        
        <!-- Roadmap Section -->
        <section id="roadmap" class="card">
            <div class="card-header">
                <div class="card-icon">
                    <i class="fas fa-map"></i>
                </div>
                <h2 class="card-title">Development Roadmap</h2>
            </div>
            
            <div class="timeline">
                <div class="timeline-item">
                    <div class="timeline-date">Q2 2024</div>
                    <h3>Near-Term Enhancements</h3>
                    <p>Multi-chain expansion (Solana, Polygon, Arbitrum), advanced ML features, real-time alerting, enhanced visualization.</p>
                </div>
                
                <div class="timeline-item">
                    <div class="timeline-date">Q3-Q4 2024</div>
                    <h3>Mid-Term Objectives</h3>
                    <p>Institutional dashboard with RBAC, backtesting framework, RESTful API microservice, regulatory compliance module.</p>
                </div>
                
                <div class="timeline-item">
                    <div class="timeline-date">2025+</div>
                    <h3>Long-Term Vision</h3>
                    <p>Cross-platform mobile apps, predictive threat intelligence, decentralized oracle networks, quantitative strategy engine.</p>
                </div>
            </div>
        </section>
        
        <!-- Author Section -->
        <section id="author" class="card" style="background: linear-gradient(135deg, rgba(15,23,42,0.9) 0%, rgba(30,41,59,0.9) 100%);">
            <div class="card-header">
                <div class="card-icon">
                    <i class="fas fa-user"></i>
                </div>
                <h2 class="card-title">About the Author</h2>
            </div>
            
            <div style="display: flex; align-items: center; flex-wrap: wrap; gap: 30px;">
                <div style="flex: 1; min-width: 300px;">
                    <h3 style="color: var(--accent); margin-bottom: 10px;">Ernest Kofi Antwi</h3>
                    <p style="margin-bottom: 15px;"><strong>Senior Software Engineer | 15+ Years Enterprise Experience</strong></p>
                    <p>Enterprise software engineer with extensive experience at Microsoft, Tesla, and Disney. Specializes in secure, scalable systems architecture with focus on blockchain intelligence, AI integration, and national security applications. U.S. Army veteran with security clearance eligibility.</p>
                    
                    <div style="margin-top: 20px;">
                        <div class="badge badge-primary">Microsoft</div>
                        <div class="badge badge-secondary">Tesla</div>
                        <div class="badge badge-success">Disney</div>
                        <div class="badge badge-warning">U.S. Army</div>
                    </div>
                </div>
                
                <div style="flex: 0 0 auto;">
                    <div style="background: linear-gradient(135deg, var(--primary) 0%, var(--secondary) 100%); padding: 3px; border-radius: 50%;">
                        <div style="width: 150px; height: 150px; background: var(--dark); border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 3rem;">
                            <i class="fas fa-user-shield"></i>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <!-- Footer -->
    <footer class="footer">
        <div class="container">
            <h2 style="margin-bottom: 20px; color: var(--accent);">Connect & Collaborate</h2>
            
            <div class="social-links">
                <a href="https://github.com/ErnestAntwi" class="social-link" title="GitHub">
                    <i class="fab fa-github"></i>
                </a>
                <a href="https://linkedin.com/in/ernest-antwi" class="social-link" title="LinkedIn">
                    <i class="fab fa-linkedin"></i>
                </a>
                <a href="mailto:ErnestK.Antwi2013@zoho.com" class="social-link" title="Email">
                    <i class="fas fa-envelope"></i>
                </a>
                <a href="#" class="social-link" title="Portfolio">
                    <i class="fas fa-globe"></i>
                </a>
            </div>
            
            <p style="color: #94a3b8; margin-top: 20px;">
                <i class="fas fa-shield-alt" style="margin-right: 8px;"></i>
                "Architecting secure, intelligent systems at the intersection of blockchain, AI, and national security."
            </p>
            
            <p style="color: #64748b; margin-top: 30px; font-size: 0.9rem;">
                © 2024 Ernest Kofi Antwi. This project is licensed under MIT License.
                <br>For demonstration and research purposes only. Not financial advice.
            </p>
        </div>
    </footer>

    <!-- JavaScript for interactivity -->
    <script>
        // Smooth scrolling for anchor links
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                e.preventDefault();
                
                const targetId = this.getAttribute('href');
                if(targetId === '#') return;
                
                const targetElement = document.querySelector(targetId);
                if(targetElement) {
                    window.scrollTo({
                        top: targetElement.offsetTop - 80,
                        behavior: 'smooth'
                    });
                }
            });
        });
        
        // Add animation to cards on scroll
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if(entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, observerOptions);
        
        // Observe all cards for animation
        document.querySelectorAll('.card, .feature-item').forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(20px)';
            el.style.transition = 'opacity 0.5s ease, transform 0.5s ease';
            observer.observe(el);
        });
        
        // Initialize tooltips
        document.querySelectorAll('.social-link').forEach(link => {
            link.addEventListener('mouseenter', function() {
                const title = this.getAttribute('title');
                if(title) {
                    const tooltip = document.createElement('div');
                    tooltip.className = 'tooltip';
                    tooltip.textContent = title;
                    tooltip.style.position = 'absolute';
                    tooltip.style.background = 'rgba(15, 23, 42, 0.9)';
                    tooltip.style.color = 'white';
                    tooltip.style.padding = '5px 10px';
                    tooltip.style.borderRadius = '4px';
                    tooltip.style.fontSize = '0.8rem';
                    tooltip.style.zIndex = '1000';
                    
                    const rect = this.getBoundingClientRect();
                    tooltip.style.top = (rect.top - 30) + 'px';
                    tooltip.style.left = (rect.left + rect.width/2 - tooltip.offsetWidth/2) + 'px';
                    
                    document.body.appendChild(tooltip);
                    this.tooltip = tooltip;
                }
            });
            
            link.addEventListener('mouseleave', function() {
                if(this.tooltip) {
                    document.body.removeChild(this.tooltip);
                    this.tooltip = null;
                }
            });
        });
    </script>
</body>
</html>
