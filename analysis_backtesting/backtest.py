class Backtester:
    def __init__(self, strategy, data):
        self.strategy = strategy
        self.data = data

    def run(self):
        """
        Run the backtest.
        """
        print("Running backtest...")
        # Placeholder logic
        for index, row in self.data.iterrows():
            signal = self.strategy.generate_signals(row)
            print(f"Date: {index}, Signal: {signal}")
        
        print("Backtest completed.")
        return {}
