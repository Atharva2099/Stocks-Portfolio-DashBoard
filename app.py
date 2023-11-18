import yfinance as yf
import pandas as pd
import numpy as np
import streamlit as st
from datetime import datetime as dt

st.write("# Indian Stock Exchange Web APP")

end_date = dt.now().strftime('%Y-%m-%d')

automobile_symbols_NSE = ["TATAMOTORS.NS","BAJAJ-AUTO.NS", "TVSMOTOR.NS", "MARUTI.NS"]
automobile_symbols_BSE = ["TATAMOTORS.BO","BAJAJ-AUTO.BO", "TVSMOTOR.BO", "MARUTI.BO"]

automobile_data_NSE = {}

for symbol in automobile_symbols_NSE:
    company_data = yf.Ticker(symbol)
    history = company_data.history(period='1d', start='2010-5-31', end=end_date)
    automobile_data_NSE[symbol] = history

for symbol, data in automobile_data_NSE.items():
    st.write(f"## {symbol} Data")
    st.write("""
    ### Closing Price National Stock Exchange
    """)
    st.line_chart(data['Close'], use_container_width=True, color="#AA00FF")
    st.write("""
    ### Volume National Stock Exchange
    """)
    st.line_chart(data['Volume'], use_container_width=True,color="#AAFF80")
    

automobile_data_BSE = {}

for symbol in automobile_symbols_BSE:
    company_data = yf.Ticker(symbol)
    history = company_data.history(period='1d', start='2010-5-31', end=end_date)
    automobile_data_NSE[symbol] = history

for symbol, data in automobile_data_BSE.items():
    st.write(f"## {symbol} Data")
    st.write("""
    ### Closing Price Mumbai Stock Exchange
    """)
    st.line_chart(data['Close'], use_container_width=True,color= "#AA00FF")
    st.write("""
    ### Volume Mumbai Stock Exchange
    """)
    st.line_chart(data['Volume'], use_container_width=True,color= "#AAFF80")