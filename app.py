# filename: app.py

import streamlit as st
import yfinance as yf

st.set_page_config(page_title="Buffett-Style Stock App", layout="centered")
st.title("📈 Buffett-Style Stock Analyzer (India)")

stock_input = st.text_input("Enter Indian Stock Symbol (e.g., TATAELXSI.NS):")

if stock_input:
    try:
        stock = yf.Ticker(stock_input)
        info = stock.info

        st.subheader(f"🔍 Analyzing {info['shortName']}")

        pe = info.get("trailingPE")
        roe = info.get("returnOnEquity", 0) * 100 if info.get("returnOnEquity") else None
        debt_to_equity = info.get("debtToEquity")

        st.write(f"**P/E Ratio**: {pe}")
        st.write(f"**ROE**: {roe:.2f}%" if roe else "ROE: Data not available")
        st.write(f"**Debt/Equity**: {debt_to_equity}" if debt_to_equity else "Debt/Equity: Data not available")

        if roe and roe > 15 and pe and pe < 25 and (debt_to_equity is None or debt_to_equity < 50):
            st.success("✅ This may be a Buffett-style stock!")
        else:
            st.warning("⚠️ Doesn't meet Buffett’s ideal metrics.")
    except:
        st.error("❌ Could not fetch stock data. Please check the symbol.")
