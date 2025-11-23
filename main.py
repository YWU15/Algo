from data_fetching.fetch_market_data import DataFetcher
from analysis_backtesting.strategy import Strategy
from analysis_backtesting.backtest import Backtester
from execution.order_manager import OrderManager
import config

def main():
    print("Starting Quant Trading System...")

    # 1. Fetch Data
    fetcher = DataFetcher()
    data = fetcher.fetch_historical_data("AAPL", "2023-01-01", "2023-12-31")

    # 2. Analysis and Backtesting
    strategy = Strategy("MeanReversion")
    backtester = Backtester(strategy, data)
    results = backtester.run()

    # 3. Execution (if live)
    if config.LIVE_TRADING:
        manager = OrderManager()
        # Example usage
        signal = strategy.generate_signals(data) # Simplified
        if signal == "BUY":
            manager.place_order("AAPL", 10, "MARKET", "BUY")

if __name__ == "__main__":
    main()
