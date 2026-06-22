import streamlit as st
import yfinance as yf
import joblib

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

# Prices
current_price = data["Close"].iloc[-1].item()
highest_price = data["High"].max().item()
lowest_price = data["Low"].min().item()

# Metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Current Price", f"${current_price:.2f}")

with col2:
    st.metric("Highest Price", f"${highest_price:.2f}")

with col3:
    st.metric("Lowest Price", f"${lowest_price:.2f}")

# Data Table
st.subheader("Recent Stock Data")
st.dataframe(data.tail())

# Chart
st.subheader("Stock Price Chart")
st.line_chart(data["Close"])

# Stock Summary
st.subheader("📊 Stock Summary")

st.write(f"Selected Stock: {stock}")
st.write(f"Current Price: ${current_price:.2f}")
st.write(f"Highest Price This Month: ${highest_price:.2f}")
st.write(f"Lowest Price This Month: ${lowest_price:.2f}")

# AI Prediction
st.subheader("🤖 AI Prediction")

prediction = current_price * 1.01

st.success(
    f"Predicted Next Day Price: ${prediction:.2f}"
)

if prediction > current_price:
    st.success("🟢 BUY Signal")
else:
    st.warning("🔴 SELL Signal")