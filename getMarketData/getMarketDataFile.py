

from tvDatafeed import TvDatafeedLive, Interval
username = ''
password = ''

tv = TvDatafeedLive()





def getMarketData(symbols,exchange,n_bars):
    marketDataDict = {}
    for symbol in symbols:

        h4_data = tv.get_hist(symbol=symbol, exchange=exchange, interval=Interval.in_5_minute, n_bars=n_bars)
        marketDataDict[symbol] = h4_data
    
    return marketDataDict












# if __name__ == "__main__":
#     # To run an async function, you need to use asyncio.run()
#     asyncio.run(main())


