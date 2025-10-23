# Binance Futures Trading Bot

## Overview
A CLI-based trading bot for **Binance USDT-M Futures** that supports multiple order types, input validation, and robust logging.  

This project demonstrates core trading functionalities as well as advanced strategies, designed for **Testnet use only**.  

### Features
- **Core Orders (Mandatory)**
  - Market Orders
  - Limit Orders
- **Advanced Orders (Bonus)**
  - Stop-Limit Orders
  - OCO (One-Cancels-the-Other)
  - TWAP (Time-Weighted Average Price)
- **Validation & Logging**
  - Validates trading pair, side, quantity, and price thresholds
  - Logs all order executions and errors to `logs/bot.log`

---

## Setup Instructions

1. **Clone the repository or extract the `.zip`**

```bash
git clone [your_repo_url]
cd new_binance_bot

2. **Create a virtual environment**

python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # macOS/Linux

3. **Install required packages**

pip install -r requirements.txt

Run the bot from the project root:

python src/main.py

Command-Line Interface (CLI) Workflow

Enter trading pair (e.g., BTCUSDT)
Enter side (BUY or SELL)
Enter order type:
MARKET
LIMIT
STOP-LIMIT
TWAP
OCO
Enter quantity (e.g., 0.001)
Enter additional parameters if required:
Limit orders: Limit price
Stop-Limit: Stop price and Limit price
TWAP: Number of slices and delay between slices
OCO: Take-profit price and Stop-loss price

Example: Market Order

Enter trading pair: BTCUSDT
Enter side: BUY
Enter order type: MARKET
Enter quantity: 0.001


Example: TWAP Order

Enter trading pair: BTCUSDT
Enter side: BUY
Enter order type: TWAP
Enter quantity: 0.01
Enter number of slices: 5
Enter delay between slices in seconds: 10
