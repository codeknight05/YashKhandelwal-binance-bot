from binance.client import Client
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Get keys from environment
API_KEY = os.getenv("BINANCE_API_KEY")
API_SECRET = os.getenv("BINANCE_API_SECRET")

if not API_KEY or not API_SECRET:
    raise SystemExit("API key or secret not found. Check your .env file.")

# Create Binance client for Testnet
client = Client(API_KEY, API_SECRET, testnet=True)

# Make sure it connects to the Testnet Futures URL
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

# Try fetching exchange info to test connection
info = client.futures_exchange_info()

print("✅ Connected to Binance Futures Testnet!")
print("Available symbols:", [s['symbol'] for s in info['symbols'][:5]])
