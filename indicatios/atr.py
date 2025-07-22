import pandas as pd

def atr_stoploss(data: pd.DataFrame, length: int = 14, multiplier: float = 1.5, smoothing: str = "RMA" , newTrend:str="sideWays"):
    high = data['high']
    low = data['low']
    close = data['close']

    # Calculate True Range (TR)
    prev_close = close.shift(1)
    tr = pd.concat([
        high - low,
        (high - prev_close).abs(),
        (low - prev_close).abs()
    ], axis=1).max(axis=1)

    # Choose smoothing method
    if smoothing == "RMA":
        atr = tr.ewm(alpha=1/length, adjust=False).mean()
    elif smoothing == "SMA":
        atr = tr.rolling(window=length).mean()
    elif smoothing == "EMA":
        atr = tr.ewm(span=length, adjust=False).mean()
    elif smoothing == "WMA":
        weights = range(1, length + 1)
        atr = tr.rolling(length).apply(lambda x: sum(weights * x) / sum(weights), raw=True)
    else:
        raise ValueError("Invalid smoothing type. Choose from: RMA, SMA, EMA, WMA")

    # Calculate stop losses
    short_stop = high + (atr * multiplier)
    long_stop = low - (atr * multiplier)
    if(newTrend=="buy_signal"):
        return float(long_stop.iloc[-2])
    elif (newTrend=="sell_signal"):
        return float(short_stop.iloc[-2])
    else :
        return None
