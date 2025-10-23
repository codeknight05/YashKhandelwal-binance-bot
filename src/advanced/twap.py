# src/advanced/twap.py
import time
import logging

def place_twap_order(client, symbol, side, total_quantity, intervals=5, delay=10):
    slice_qty = total_quantity / intervals
    print(f"⚡ TWAP order: {total_quantity} {symbol} in {intervals} slices ({slice_qty} per slice)")

    for i in range(1, intervals+1):
        try:
            order = client.futures_create_order(
                symbol=symbol,
                side=side,
                type='MARKET',
                quantity=slice_qty
            )
            logging.info(f"TWAP slice {i} executed: {order}")
            print(f"✅ Slice {i}/{intervals} executed: {slice_qty} {symbol}")
        except Exception as e:
            logging.error(f"TWAP slice {i} failed: {e}")
            print(f"❌ Slice {i} failed: {e}")
        time.sleep(delay)
    print("✅ TWAP order complete!")
