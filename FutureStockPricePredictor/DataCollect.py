import yfinance as yf
# Gathering of Stock Data
tickerSymbol = 'AMD' # TSLA -> TESLA 
close_data = []
tickerData = yf.Ticker(tickerSymbol)
todayData = tickerData.history(period='5y')
#Appending Closing Prices
for i in range(1258):
  close_data.append(todayData['Close'][i])
