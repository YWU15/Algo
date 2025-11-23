import schwabdev
import os
from dotenv import load_dotenv

class OrderManager:
    def __init__(self):
        load_dotenv()
        app_key = os.getenv('SCHWAB_APP_KEY')
        app_secret = os.getenv('SCHWAB_APP_SECRET')
        
        if app_key and app_secret:
            self.client = schwabdev.Client(app_key, app_secret)
            print("Schwab client initialized.")
        else:
            print("Warning: SCHWAB_APP_KEY or SCHWAB_APP_SECRET not found in environment.")
            self.client = None

    def place_order(self, symbol, quantity, order_type="MARKET", action="BUY"):
        """
        Place an order using Schwab API.
        """
        print(f"Placing {action} order for {quantity} shares of {symbol} at {order_type}")
        if self.client:
            # Placeholder for actual API call
            # self.client.order_place(...)
            pass
        else:
            print("Client not initialized, cannot place order.")
