import yfinance as yf
#yahoo finance function test
msft = yf.Ticker("MSFT")
print(msft)
print(msft.info)
print(msft.history(period="max"))