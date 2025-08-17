import time
from indicatios.ema import ema
from indicatios.atr import atr_stoploss
from getMarketData.getMarketDataFile import getMarketData
from businesslogic.logic import botLogic
from sendMessage.sendMessage import send_message


def bot():
    print("🚀 Testing Trend Detection for multiple pairs...\n")

    symbols = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT']  # Add more if needed
    fullData = getMarketData(symbols=symbols, exchange="BINANCE", n_bars=4500)

    for symbol in symbols:
        print(f"\n📊 Checking {symbol}...\n")

        if symbol not in fullData or fullData[symbol] is None:
            print(f"⚠️ No data found for {symbol}")
            continue

        df = fullData[symbol]

        if df is None or df.empty:
            print(f"⚠️ Empty DataFrame for {symbol}")
            continue

        if len(df) < 4000:
            print(f"❌ Not enough data for {symbol}: only {len(df)} rows, need at least 4000.")
            continue

        for i in range(len(df), 3499, -1):
            window = df[i-500:i]

            if window.empty or len(window) < 500:
                print(f"⚠️ Skipping {symbol}, i={i}, not enough candles in window.")
                continue

            marketDataByPair = {symbol: window}
            signal = botLogic(marketDataByPair , symbol=symbol)
            candle_time = window.index[-1] if not window.empty else "N/A"

            if signal is not None:
                print(f"✅ {symbol} | Time={candle_time}, i={i}, Signal={signal['signal']} , SL={signal['SL']}")

        # Optional: sleep between different symbols
        time.sleep(10)  # wait 10 seconds before starting next symbol

    print("\n🚀 Done scanning all symbols.")
bot()