import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App
Shown are the stock **closing price** and ***volume*** of Tesla!
""")
# Add a selectbox for the ticker symbol
tickerSymbol = st.selectbox('Select ticker symbol', ['TSLA', 'AAPL', 'GOOGL', 'MSFT', 'AMZN', 'META', 'NFLX', 'TSM', 'NVDA', 'PYPL'])

# Add date input widgets for the start and end dates
start_date = st.date_input('Start date', pd.to_datetime('2010-05-31'))
end_date = st.date_input('End date', pd.to_datetime('2024-12-18'))

# Get data on the selected ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for the selected ticker
tickerDf = tickerData.history(period='1d', start=start_date, end=end_date)

# Display the closing price and volume charts
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)