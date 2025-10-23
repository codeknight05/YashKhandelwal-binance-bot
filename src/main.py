# src/main.py
import os
import logging
from dotenv import load_dotenv
from binance.client import Client
from market_orders import place_market_order
from limit_orders import place_limit_order
from advanced.twap import place_twap_order
from advanced.stop_limit import place_stop_limit_order
from advanced.oco import place_oco_order

load_dotenv()

# Logging setup
if not os.path.exists("logs"):
    os.makedirs("logs")
logging.basicConfig(filename='logs/bot.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

if not API_KEY or not API_SECRET:
    print("❌ API key or secret not found in .env")
    exit()

client = Client(API_KEY, API_SECRET, testnet=True)
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

print("✅ Connected to Binance Futures Testnet!")

while True:
    print("\n--- New Order ---")
    symbol = input("Enter trading pair (e.g., BTCUSDT): ").upper()
    side = input("Enter side (BUY/SELL): ").upper()
    order_type = input("Enter order type (MARKET, LIMIT, STOP-LIMIT, TWAP, OCO): ").upper()
    quantity = float(input("Enter quantity: "))

    order = None

    if order_type == "MARKET":
        order = place_market_order(client, symbol, side, quantity)
    elif order_type == "LIMIT":
        price = float(input("Enter limit price: "))
        order = place_limit_order(client, symbol, side, quantity, price)
    elif order_type == "STOP-LIMIT":
        stop_price = float(input("Enter stop price: "))
        limit_price = float(input("Enter limit price: "))
        order = place_stop_limit_order(client, symbol, side, quantity, stop_price, limit_price)
    elif order_type == "TWAP":
        intervals = int(input("Enter number of slices (e.g., 5): "))
        delay = int(input("Enter delay between slices in seconds (e.g., 10): "))
        place_twap_order(client, symbol, side, quantity, intervals, delay)
        order = True
    elif order_type == "OCO":
        take_profit = float(input("Enter take-profit price: "))
        stop_loss = float(input("Enter stop-loss price: "))
        place_oco_order(client, symbol, side, quantity, take_profit, stop_loss)
        order = True

    if order:
        print("✅ Order processed. Check logs for details.")
    cont = input("Place another order? (y/n): ").lower()
    if cont != 'y':
        break
