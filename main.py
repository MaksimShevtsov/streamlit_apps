import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
#Simple Stock Price App

Shown are the stock closing price and volume of Google!

""")

# define the ticker symbol
tickerSymbol = 'GOOGL'
# get data on this ticker
tikerData = yf.Ticker(tickerSymbol)
# get the histirical prices for this ticker
tickerDf = tikerData.history(periad='id', start='2010-5-31', end='2021-8-30')

st.write('''
## Closing Price
''')
st.line_chart(tickerDf.Close)
st.write('''
## Volume Price
''')
st.line_chart(tickerDf.Volume)