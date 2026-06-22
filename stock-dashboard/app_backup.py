import streamlit as st
import yfinance as yf

st.set_page_config(
    page_title="AI Stock Market Intelligence Dashboard",
    layout="wide"
)

st.title("📈 AI Stock Market Intelligence Dashboard")

stock = st.selectbox(
    "Select a Stock",
    ["AAPL", "MSFT", "GOOGL", "TSLA"]
)

# Download stock data
data = yf.download(stock, period="1mo")

# Show data
st.subheader("Recent Stock Data")
st.dataframe(data.tail())

# Get values safely
close_prices = data["Close"]
high_prices = data["High"]
low_prices = data["Low"]

current_price = close_prices.iloc[-1]
highest_price = high_prices.max()
lowest_price = low_prices.min()

# Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Current Price", f"${current_price}")

with col2:
    st.metric("Highest Price", f"${highest_price}")

with col3:
    st.metric("Lowest Price", f"${lowest_price}")

# Chart
st.subheader("Stock Price Chart")
st.line_chart(close_prices)