import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

df = yf.download("MSFT", start="2020-01-01", end="2022-12-31")
df[["Open", "Close"]].plot()
plt.show()
