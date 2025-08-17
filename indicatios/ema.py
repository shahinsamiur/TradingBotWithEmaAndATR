
def ema(data, symbol, column='close', length=50):
    df = data[symbol]
    prices = df[column].tolist()
    k = 2 / (length + 1)
    ema_val = prices[0]
    for price in prices[1:]:
        ema_val = (price * k) + (ema_val * (1 - k))

    return ema_val
