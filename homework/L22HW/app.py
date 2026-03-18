# Ty Cockerham | Student ID: U0000023539

import streamlit as st
import requests
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Crypto Dashboard", layout="wide")
st.title("Cryptocurrency Dashboard")

st.sidebar.header("Controls")

coin = st.sidebar.selectbox("Select Coin", ["bitcoin", "ethereum", "solana", "dogecoin"])

days = st.sidebar.slider("Price History (days)", 7, 90, 30)

@st.cache_data(ttl=300)
def fetch_markets():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {"vs_currency": "usd", "order": "market_cap_desc", "per_page": 10}
    response = requests.get(url, params=params)
    if response.status_code != 200:
        return None
    return response.json()

@st.cache_data(ttl=300)
def fetch_price_history(coin_id, days):
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/market_chart"
    params = {"vs_currency": "usd", "days": days}
    response = requests.get(url, params=params)
    if response.status_code != 200:
        return None
    return response.json()

market_data = fetch_markets()
history_data = fetch_price_history(coin, days)

if market_data is None or history_data is None:
    st.error("❌ Failed to load data from CoinGecko. Please try again later.")
    st.stop()

df_market = pd.DataFrame(market_data)

df_history = pd.DataFrame(history_data["prices"], columns=["timestamp", "price"])
df_history["timestamp"] = pd.to_datetime(df_history["timestamp"], unit="ms")
df_history = df_history.set_index("timestamp")

current = df_market[df_market["id"] == coin].iloc[0]

col1, col2, col3 = st.columns(3)

col1.metric("Current Price", f"${current['current_price']:,.2f}", f"{current['price_change_percentage_24h']:.2f}%")
col2.metric("Market Cap",    f"${current['market_cap']:,.0f}")
col3.metric("24h Volume",    f"${current['total_volume']:,.0f}")

st.subheader(f"{coin.capitalize()} Price — Last {days} Days")

fig = px.line(df_history, y="price", labels={"price": "Price (USD)"})
st.plotly_chart(fig, width='stretch')

st.subheader("Top 10 Coins by Market Cap")

fig_bar = px.bar(df_market, x="name", y="market_cap", labels={"market_cap": "Market Cap (USD)", "name": "Coin"})
st.plotly_chart(fig_bar, width='stretch')

st.subheader("Market Data Table")
st.dataframe(df_market[["name", "current_price", "market_cap", "price_change_percentage_24h"]].round(2))