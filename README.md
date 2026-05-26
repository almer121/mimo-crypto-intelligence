<div align="center">

# 🚀 mimo-crypto-intelligence

**AI-Powered Crypto Intelligence System Built with Xiaomi MiMo**

*Real-time memecoin analysis • Multi-layer risk detection • Smart trader tracking*

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg?style=for-the-badge)](LICENSE)
[![MiMo Powered](https://img.shields.io/badge/MiMo-100T-orange.svg?style=for-the-badge)](https://github.com/XiaomiMiMo/MiMo)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg?style=for-the-badge)](tests/)

---

<p align="center">
  <strong>🎯 One-command crypto intelligence for Solana memecoins</strong><br>
  <sub>From token discovery to risk assessment in seconds</sub>
</p>

[Features](#-features) • [Quick Start](#-quick-start) • [Architecture](#-architecture) • [CLI](#-cli-commands) • [Reports](#-reports) • [Contributing](#-contributing)

</div>

---

## 📊 Why mimo-crypto-intelligence?

The memecoin market moves at lightspeed. By the time you manually check a token's liquidity, dev history, bundle patterns, and social presence — the opportunity is gone. 

**mimo-crypto-intelligence** does all of this in **under 5 seconds**, powered by **Xiaomi MiMo** for intelligent decision-making.

<table>
<tr>
<td width="50%">

### ❌ Without mimo-crypto-intelligence
- Manual checking on multiple sites
- Miss rug pulls hidden in bundles
- No trader pattern tracking
- Guesswork on entry timing
- Hours wasted per token analysis

</td>
<td width="50%">

### ✅ With mimo-crypto-intelligence
- **One command** full analysis
- **12-layer** rug detection system
- **Real-time** smart money tracking
- **Data-driven** entry recommendations
- **Seconds** per token analysis

</td>
</tr>
</table>

---

## 🎯 Features

### 🔍 Token Discovery Engine
```
┌─────────────────────────────────────────────────────────┐
│  Pump.fun API → DexScreener → Jupiter → Smart Filter    │
└─────────────────────────────────────────────────────────┘
                         ↓
        ┌────────────────────────────────┐
        │  • Market Cap: $20K - $300K    │
        │  • Liquidity: $3K - $100K      │
        │  • Age: 5min - 4h              │
        │  • Buy Ratio: ≥45%             │
        │  • Min 50 txns/hour            │
        └────────────────────────────────┘
```

### 🛡️ 12-Layer Risk Detection System

| # | Risk Method | Detection | Severity |
|---|-------------|-----------|----------|
| 1 | Bundle Dump | Whale wallet clustering | 🔴 Critical |
| 2 | Liquidity Pull | LP removal monitoring | 🔴 Critical |
| 3 | Mint Authority | Token permission check | 🟡 Warning |
| 4 | Freeze/Honeypot | Transfer restriction test | 🔴 Critical |
| 5 | Wash Trading | Volume-to-txn ratio | 🟠 High |
| 6 | Cabal Play | Insider wallet patterns | 🟠 High |
| 7 | Honeypot Program | Contract simulation | 🔴 Critical |
| 8 | Burn Scam | Fake LP burn claims | 🟡 Warning |
| 9 | Social Engineering | Twitter/Discord analysis | 🟡 Warning |
| 10 | Fee Extraction | Dynamic fee detection | 🟠 High |
| 11 | Ad Timing | Promo-pump correlation | 🟡 Warning |
| 12 | Speed Rug | Sub-5min rug detection | 🔴 Critical |

### 👥 Smart Trader Tracking

```
Real-time monitoring of successful wallets:
├── Entry patterns
├── Position sizing
├── Hold duration
├── Win rate per wallet
└── Cross-token performance
```

### 📱 Twitter Intelligence

- **Account Scoring**: Followers, activity, bio relevance
- **Trending Detection**: Real-time crypto hashtag monitoring
- **KOL Tracking**: Influencer token mentions
- **Correlation Analysis**: Twitter presence → token success rate

*Data shows: **80% of graduated Pump.fun tokens** have active Twitter presence*

### ⛽ Gas Profitability Calculator

```
Trade Size → Gas Cost → Minimum TP → Recommended Strategy

0.01 SOL  →  93% cost  →  ❌ Not viable
0.05 SOL  →   4.5% cost →  TP ≥ 7%
0.10 SOL  →   2.3% cost →  TP ≥ 3.4%
0.50 SOL  →   0.5% cost →  TP ≥ 0.7%
```

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- Solana wallet with SOL (for real trades)
- RPC endpoint (public or private)

### Installation

```bash
# Clone the repository
git clone https://github.com/almer121/mimo-crypto-intelligence.git
cd mimo-crypto-intelligence

# Install dependencies
pip install -e ".[dev]"

# Or install manually
pip install httpx base58 solders solana websocket-client
```

### First Run

```bash
# Analyze a specific token
python3 mimo_crypto.py analyze --token 7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU --risk

# Discover trending tokens
python3 mimo_crypto.py discover --limit 10

# Monitor tokens real-time (15 minutes)
python3 mimo_crypto.py monitor --discover --duration 15

# Generate comprehensive report
python3 mimo_crypto.py report --type comprehensive
```

### Environment Variables

```bash
# Optional: Private RPC for better performance
export SOLANA_RPC_URL="https://api.mainnet-beta.solana.com"

# Optional: Telegram for reports
export TELEGRAM_BOT_TOKEN="your_bot_token"
export TELEGRAM_CHAT_ID="your_chat_id"
```

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    mimo-crypto-intelligence                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │   Token      │  │   Risk       │  │   Trader     │          │
│  │   Discovery  │  │   Analyzer   │  │   Tracker    │          │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘          │
│         │                 │                 │                    │
│         ▼                 ▼                 ▼                    │
│  ┌─────────────────────────────────────────────────────┐        │
│  │              Data Aggregation Layer                   │        │
│  └─────────────────────────────────────────────────────┘        │
│         │                 │                 │                    │
│         ▼                 ▼                 ▼                    │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │  Pump.fun    │  │  DexScreener │  │  Twitter     │          │
│  │  WebSocket   │  │  REST API    │  │  Scraper     │          │
│  └──────────────┘  └──────────────┘  └──────────────┘          │
│                                                                  │
│  ┌─────────────────────────────────────────────────────┐        │
│  │              Intelligence Engine (MiMo)              │        │
│  └─────────────────────────────────────────────────────┘        │
│         │                                                        │
│         ▼                                                        │
│  ┌─────────────────────────────────────────────────────┐        │
│  │           Report Generator (Telegram/Discord)         │        │
│  └─────────────────────────────────────────────────────┘        │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

---

## 💻 CLI Commands

### Analyze Token

```bash
# Full risk analysis
python3 mimo_crypto.py analyze --token <MINT> --risk

# Quick check
python3 mimo_crypto.py analyze --token <MINT>

# With Twitter analysis
python3 mimo_crypto.py analyze --token <MINT> --twitter
```

### Discover Tokens

```bash
# Find trending tokens
python3 mimo_crypto.py discover --limit 20

# With specific filters
python3 mimo_crypto.py discover --min-mcap 20000 --max-mcap 300000
```

### Monitor Mode

```bash
# Real-time monitoring with auto-discovery
python3 mimo_crypto.py monitor --discover --duration 30

# Monitor specific tokens
python3 mimo_crypto.py monitor --tokens <MINT1> <MINT2> --duration 60
```

### Generate Reports

```bash
# Comprehensive report
python3 mimo_crypto.py report --type comprehensive

# Quick summary
python3 mimo_crypto.py report --type quick

# Risk-focused report
python3 mimo_crypto.py report --type risk
```

---

## 📊 Reports

Reports are designed for **Telegram** and **Discord** with clean, scannable format:

```
🔍 MIKRO-SCREENER ACTIVE
━━━━━━━━━━━━━━━━━━━━━━━━
📊 30 token termonitor
🔥 3 trending (>500 txns/h)
🛡️ 11 lolos filter (36.7%)
⏱️ Scan: 0.9s

📈 TOP ACTIVE TOKENS:
  • $HOLYBANK — 21,658 txns/h | MC: $53K
  • $Yorigami — 14,296 txns/h | MC: $45K  
  • $ELUN — 9,254 txns/h | MC: $78K
```

---

## ⚡ Performance

| Metric | Value |
|--------|-------|
| Token Analysis | < 5 seconds |
| Risk Assessment | < 3 seconds |
| Discovery Scan | < 10 seconds |
| WebSocket Latency | < 100ms |
| API Calls/minute | ~50 (rate-limited) |

---

## 🛠️ Tech Stack

- **Language**: Python 3.10+
- **AI Engine**: Xiaomi MiMo 100T
- **Blockchain**: Solana (via solders/solana-py)
- **Data Sources**: 
  - Pump.fun WebSocket API
  - DexScreener REST API
  - Jupiter Aggregator
  - Twitter/X API
- **Reporting**: Telegram Bot API
- **Testing**: pytest

---

## 📈 Real-World Results

Tested with live Solana memecoin data:

- ✅ **$WAIFU**: Detected +7.9% opportunity, flagged low risk
- ✅ **$HOLYBANK**: Identified as high-activity (21,658 txns/h)
- ✅ **$BUFF**: Scored 65/100 investment potential
- ✅ **Bundle Detection**: Caught $Patriot (-33% dump pattern)
- ✅ **Liquidity Pull**: Flagged $DAE6900 (-52.8% rug)

---

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

```bash
# Fork & Clone
git clone https://github.com/YOUR_USERNAME/mimo-crypto-intelligence.git

# Create feature branch
git checkout -b feature/amazing-feature

# Make changes & test
python -m pytest tests/

# Submit PR
git push origin feature/amazing-feature
```

---

## 📜 License

MIT License - see [LICENSE](LICENSE) for details.

---

## 🙏 Acknowledgments

- **Xiaomi MiMo Team** for the powerful 100T model
- **Pump.fun** for the memecoin ecosystem
- **DexScreener** for real-time market data
- **Jupiter Aggregator** for Solana liquidity
- **Solana Foundation** for the blockchain infrastructure

---

<div align="center">

**Built with ❤️ and Xiaomi MiMo**

*Making memecoin trading intelligent, one token at a time*

[⬆ Back to top](#-mimo-crypto-intelligence)

</div>
