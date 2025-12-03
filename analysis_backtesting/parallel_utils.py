import pandas as pd

def process_chunk(chunk):
    chunk = chunk.copy()
    pattern = r'O:?([A-Z]+)(\d{6})([CP])(\d{8})'
    extracted = chunk['ticker'].str.extract(pattern)
    chunk['ticker_symbol'] = extracted[0]
    chunk['expiration'] = pd.to_datetime(extracted[1], format='%y%m%d')
    chunk['option_type'] = extracted[2].map({'C': 'call', 'P': 'put'})
    chunk['strike'] = pd.to_numeric(extracted[3]) / 1000.0
    return chunk
