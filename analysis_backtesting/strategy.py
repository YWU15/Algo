class Strategy:
    def __init__(self, name):
        self.name = name

    def generate_signals(self, data):
        """
        Analyze data and generate trading signals.
        """
        print(f"Generating signals using strategy: {self.name}")
        # Placeholder: Return 'BUY', 'SELL', or 'HOLD'
        return "HOLD"
