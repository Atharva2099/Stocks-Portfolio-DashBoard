import yfinance as yf
import pandas as pd
import numpy as np
import streamlit as st
from datetime import datetime as dt

st.write("# Indian Stock Exchange Web APP")

end_date = dt.now().strftime('%Y-%m-%d')

# Get user input for NSE and BSE stocks
stock_NSE = st.text_input("Enter NSE Stock:")
stock_BSE = st.text_input("Enter BSE Stock:")

# Combine user input with stock exchange suffix
Stock_NSE = stock_NSE + ".NS"
Stock_BSE = stock_BSE + ".BO"

# Fetch data for NSE stock
company_data_NSE = yf.Ticker(Stock_NSE)
history_NSE = company_data_NSE.history(period='1d', start='2010-5-31', end=end_date)

# Fetch data for BSE stock
company_data_BSE = yf.Ticker(Stock_BSE)
history_BSE = company_data_BSE.history(period='1d', start='2010-5-31', end=end_date)

# Display NSE stock data
st.write(f"## {stock_NSE} Data")
st.write("""
### Closing Price National Stock Exchange
""")
st.line_chart(history_NSE['Close'], use_container_width=True, color="#AA00FF")
st.write("""
### Volume National Stock Exchange
""")
st.line_chart(history_NSE['Volume'], use_container_width=True, color="#AAFF80")

# Display BSE stock data
st.write(f"## {stock_BSE} Data")
st.write("""
### Closing Price Mumbai Stock Exchange
""")
st.line_chart(history_BSE['Close'], use_container_width=True, color="#AA00FF")
st.write("""
### Volume Mumbai Stock Exchange
""")
st.line_chart(history_BSE['Volume'], use_container_width=True, color="#AAFF80")
