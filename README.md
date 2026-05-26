     1|<div align="center">
     2|
     3|# 🚀 mimo-crypto-intelligence
     4|
     5|**AI-Powered Crypto Intelligence System Built with MiMo**
     6|
     7|*Real-time memecoin analysis • Multi-layer risk detection • Smart trader tracking*
     8|
     9|[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
    10|[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg?style=for-the-badge)](LICENSE)
    11|[![MiMo Powered](https://img.shields.io/badge/AI-MiMo-orange.svg?style=for-the-badge)]
    12|[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg?style=for-the-badge)](tests/)
    13|
    14|---
    15|
    16|<p align="center">
    17|  <strong>🎯 One-command crypto intelligence for Solana memecoins</strong><br>
    18|  <sub>From token discovery to risk assessment in seconds</sub>
    19|</p>
    20|
    21|[Features](#-features) • [Quick Start](#-quick-start) • [Architecture](#-architecture) • [CLI](#-cli-commands) • [Reports](#-reports) • [Contributing](#-contributing)
    22|
    23|</div>
    24|
    25|---
    26|
    27|## 📊 Why mimo-crypto-intelligence?
    28|
    29|The memecoin market moves at lightspeed. By the time you manually check a token's liquidity, dev history, bundle patterns, and social presence — the opportunity is gone. 
    30|
    31|**mimo-crypto-intelligence** does all of this in **under 5 seconds**, powered by **MiMo** for intelligent decision-making.
    32|
    33|<table>
    34|<tr>
    35|<td width="50%">
    36|
    37|### ❌ Without mimo-crypto-intelligence
    38|- Manual checking on multiple sites
    39|- Miss rug pulls hidden in bundles
    40|- No trader pattern tracking
    41|- Guesswork on entry timing
    42|- Hours wasted per token analysis
    43|
    44|</td>
    45|<td width="50%">
    46|
    47|### ✅ With mimo-crypto-intelligence
    48|- **One command** full analysis
    49|- **12-layer** rug detection system
    50|- **Real-time** smart money tracking
    51|- **Data-driven** entry recommendations
    52|- **Seconds** per token analysis
    53|
    54|</td>
    55|</tr>
    56|</table>
    57|
    58|---
    59|
    60|## 🎯 Features
    61|
    62|### 🔍 Token Discovery Engine
    63|```
    64|┌─────────────────────────────────────────────────────────┐
    65|│  Pump.fun API → DexScreener → Jupiter → Smart Filter    │
    66|└─────────────────────────────────────────────────────────┘
    67|                         ↓
    68|        ┌────────────────────────────────┐
    69|        │  • Market Cap: $20K - $300K    │
    70|        │  • Liquidity: $3K - $100K      │
    71|        │  • Age: 5min - 4h              │
    72|        │  • Buy Ratio: ≥45%             │
    73|        │  • Min 50 txns/hour            │
    74|        └────────────────────────────────┘
    75|```
    76|
    77|### 🛡️ 12-Layer Risk Detection System
    78|
    79|| # | Risk Method | Detection | Severity |
    80||---|-------------|-----------|----------|
    81|| 1 | Bundle Dump | Whale wallet clustering | 🔴 Critical |
    82|| 2 | Liquidity Pull | LP removal monitoring | 🔴 Critical |
    83|| 3 | Mint Authority | Token permission check | 🟡 Warning |
    84|| 4 | Freeze/Honeypot | Transfer restriction test | 🔴 Critical |
    85|| 5 | Wash Trading | Volume-to-txn ratio | 🟠 High |
    86|| 6 | Cabal Play | Insider wallet patterns | 🟠 High |
    87|| 7 | Honeypot Program | Contract simulation | 🔴 Critical |
    88|| 8 | Burn Scam | Fake LP burn claims | 🟡 Warning |
    89|| 9 | Social Engineering | Twitter/Discord analysis | 🟡 Warning |
    90|| 10 | Fee Extraction | Dynamic fee detection | 🟠 High |
    91|| 11 | Ad Timing | Promo-pump correlation | 🟡 Warning |
    92|| 12 | Speed Rug | Sub-5min rug detection | 🔴 Critical |
    93|
    94|### 👥 Smart Trader Tracking
    95|
    96|```
    97|Real-time monitoring of successful wallets:
    98|├── Entry patterns
    99|├── Position sizing
   100|├── Hold duration
   101|├── Win rate per wallet
   102|└── Cross-token performance
   103|```
   104|
   105|### 📱 Twitter Intelligence
   106|
   107|- **Account Scoring**: Followers, activity, bio relevance
   108|- **Trending Detection**: Real-time crypto hashtag monitoring
   109|- **KOL Tracking**: Influencer token mentions
   110|- **Correlation Analysis**: Twitter presence → token success rate
   111|
   112|*Data shows: **80% of graduated Pump.fun tokens** have active Twitter presence*
   113|
   114|### ⛽ Gas Profitability Calculator
   115|
   116|```
   117|Trade Size → Gas Cost → Minimum TP → Recommended Strategy
   118|
   119|0.01 SOL  →  93% cost  →  ❌ Not viable
   120|0.05 SOL  →   4.5% cost →  TP ≥ 7%
   121|0.10 SOL  →   2.3% cost →  TP ≥ 3.4%
   122|0.50 SOL  →   0.5% cost →  TP ≥ 0.7%
   123|```
   124|
   125|---
   126|
   127|## 🚀 Quick Start
   128|
   129|### Prerequisites
   130|
   131|- Python 3.10+
   132|- Solana wallet with SOL (for real trades)
   133|- RPC endpoint (public or private)
   134|
   135|### Installation
   136|
   137|```bash
   138|# Clone the repository
   139|git clone https://github.com/almer121/mimo-crypto-intelligence.git
   140|cd mimo-crypto-intelligence
   141|
   142|# Install dependencies
   143|pip install -e ".[dev]"
   144|
   145|# Or install manually
   146|pip install httpx base58 solders solana websocket-client
   147|```
   148|
   149|### First Run
   150|
   151|```bash
   152|# Analyze a specific token
   153|python3 mimo_crypto.py analyze --token 7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU --risk
   154|
   155|# Discover trending tokens
   156|python3 mimo_crypto.py discover --limit 10
   157|
   158|# Monitor tokens real-time (15 minutes)
   159|python3 mimo_crypto.py monitor --discover --duration 15
   160|
   161|# Generate comprehensive report
   162|python3 mimo_crypto.py report --type comprehensive
   163|```
   164|
   165|### Environment Variables
   166|
   167|```bash
   168|# Optional: Private RPC for better performance
   169|export SOLANA_RPC_URL="https://api.mainnet-beta.solana.com"
   170|
   171|# Optional: Telegram for reports
   172|export TELEGRAM_BOT_TOKEN="your_bot_token"
   173|export TELEGRAM_CHAT_ID="your_chat_id"
   174|```
   175|
   176|---
   177|
   178|## 🏗️ Architecture
   179|
   180|```
   181|┌─────────────────────────────────────────────────────────────────┐
   182|│                    mimo-crypto-intelligence                       │
   183|├─────────────────────────────────────────────────────────────────┤
   184|│                                                                  │
   185|│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
   186|│  │   Token      │  │   Risk       │  │   Trader     │          │
   187|│  │   Discovery  │  │   Analyzer   │  │   Tracker    │          │
   188|│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘          │
   189|│         │                 │                 │                    │
   190|│         ▼                 ▼                 ▼                    │
   191|│  ┌─────────────────────────────────────────────────────┐        │
   192|│  │              Data Aggregation Layer                   │        │
   193|│  └─────────────────────────────────────────────────────┘        │
   194|│         │                 │                 │                    │
   195|│         ▼                 ▼                 ▼                    │
   196|│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
   197|│  │  Pump.fun    │  │  DexScreener │  │  Twitter     │          │
   198|│  │  WebSocket   │  │  REST API    │  │  Scraper     │          │
   199|│  └──────────────┘  └──────────────┘  └──────────────┘          │
   200|│                                                                  │
   201|│  ┌─────────────────────────────────────────────────────┐        │
   202|│  │              Intelligence Engine (MiMo)              │        │
   203|│  └─────────────────────────────────────────────────────┘        │
   204|│         │                                                        │
   205|│         ▼                                                        │
   206|│  ┌─────────────────────────────────────────────────────┐        │
   207|│  │           Report Generator (Telegram/Discord)         │        │
   208|│  └─────────────────────────────────────────────────────┘        │
   209|│                                                                  │
   210|└─────────────────────────────────────────────────────────────────┘
   211|```
   212|
   213|---
   214|
   215|## 💻 CLI Commands
   216|
   217|### Analyze Token
   218|
   219|```bash
   220|# Full risk analysis
   221|python3 mimo_crypto.py analyze --token <MINT> --risk
   222|
   223|# Quick check
   224|python3 mimo_crypto.py analyze --token <MINT>
   225|
   226|# With Twitter analysis
   227|python3 mimo_crypto.py analyze --token <MINT> --twitter
   228|```
   229|
   230|### Discover Tokens
   231|
   232|```bash
   233|# Find trending tokens
   234|python3 mimo_crypto.py discover --limit 20
   235|
   236|# With specific filters
   237|python3 mimo_crypto.py discover --min-mcap 20000 --max-mcap 300000
   238|```
   239|
   240|### Monitor Mode
   241|
   242|```bash
   243|# Real-time monitoring with auto-discovery
   244|python3 mimo_crypto.py monitor --discover --duration 30
   245|
   246|# Monitor specific tokens
   247|python3 mimo_crypto.py monitor --tokens <MINT1> <MINT2> --duration 60
   248|```
   249|
   250|### Generate Reports
   251|
   252|```bash
   253|# Comprehensive report
   254|python3 mimo_crypto.py report --type comprehensive
   255|
   256|# Quick summary
   257|python3 mimo_crypto.py report --type quick
   258|
   259|# Risk-focused report
   260|python3 mimo_crypto.py report --type risk
   261|```
   262|
   263|---
   264|
   265|## 📊 Reports
   266|
   267|Reports are designed for **Telegram** and **Discord** with clean, scannable format:
   268|
   269|```
   270|🔍 MIKRO-SCREENER ACTIVE
   271|━━━━━━━━━━━━━━━━━━━━━━━━
   272|📊 30 token termonitor
   273|🔥 3 trending (>500 txns/h)
   274|🛡️ 11 lolos filter (36.7%)
   275|⏱️ Scan: 0.9s
   276|
   277|📈 TOP ACTIVE TOKENS:
   278|  • $HOLYBANK — 21,658 txns/h | MC: $53K
   279|  • $Yorigami — 14,296 txns/h | MC: $45K  
   280|  • $ELUN — 9,254 txns/h | MC: $78K
   281|```
   282|
   283|---
   284|
   285|## ⚡ Performance
   286|
   287|| Metric | Value |
   288||--------|-------|
   289|| Token Analysis | < 5 seconds |
   290|| Risk Assessment | < 3 seconds |
   291|| Discovery Scan | < 10 seconds |
   292|| WebSocket Latency | < 100ms |
   293|| API Calls/minute | ~50 (rate-limited) |
   294|
   295|---
   296|
   297|## 🛠️ Tech Stack
   298|
   299|- **Language**: Python 3.10+
   300|- **AI Engine**: MiMo
   301|- **Blockchain**: Solana (via solders/solana-py)
   302|- **Data Sources**: 
   303|  - Pump.fun WebSocket API
   304|  - DexScreener REST API
   305|  - Jupiter Aggregator
   306|  - Twitter/X API
   307|- **Reporting**: Telegram Bot API
   308|- **Testing**: pytest
   309|
   310|---
   311|
   312|## 📈 Real-World Results
   313|
   314|Tested with live Solana memecoin data:
   315|
   316|- ✅ **$WAIFU**: Detected +7.9% opportunity, flagged low risk
   317|- ✅ **$HOLYBANK**: Identified as high-activity (21,658 txns/h)
   318|- ✅ **$BUFF**: Scored 65/100 investment potential
   319|- ✅ **Bundle Detection**: Caught $Patriot (-33% dump pattern)
   320|- ✅ **Liquidity Pull**: Flagged $DAE6900 (-52.8% rug)
   321|
   322|---
   323|
   324|## 🤝 Contributing
   325|
   326|We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.
   327|
   328|```bash
   329|# Fork & Clone
   330|git clone https://github.com/YOUR_USERNAME/mimo-crypto-intelligence.git
   331|
   332|# Create feature branch
   333|git checkout -b feature/amazing-feature
   334|
   335|# Make changes & test
   336|python -m pytest tests/
   337|
   338|# Submit PR
   339|git push origin feature/amazing-feature
   340|```
   341|
   342|---
   343|
   344|## 📜 License
   345|
   346|MIT License - see [LICENSE](LICENSE) for details.
   347|
   348|---
   349|
   350|## 🙏 Acknowledgments
   351|
   352|- **MiMo Team** for the powerful model
   353|- **Pump.fun** for the memecoin ecosystem
   354|- **DexScreener** for real-time market data
   355|- **Jupiter Aggregator** for Solana liquidity
   356|- **Solana Foundation** for the blockchain infrastructure
   357|
   358|---
   359|
   360|<div align="center">
   361|
   362|**Built with ❤️ and MiMo AI**
   363|
   364|*Making memecoin trading intelligent, one token at a time*
   365|
   366|[⬆ Back to top](#-mimo-crypto-intelligence)
   367|
   368|</div>
   369|