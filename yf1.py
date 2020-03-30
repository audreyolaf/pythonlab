import yfinance as yf
#yahoo finance function test
msft = yf.Ticker("MSFT")
print(msft)
print(msft.info)
print(msft.history(period="ytd"))

data_df = yf.download("QQQ", start="2020-01-01", end="2020-03-28")
data_df.to_csv("qqq.csv")

