import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

def fetch_financial_data(symbol, start_date, end_date):
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    return stock_data

def process_data(stock_data):
    stock_data['Rolling Mean'] = stock_data['Close'].rolling(window=20).mean()
    return stock_data

def display_data(stock_data):
    st.subheader("Processed Data")
    st.write(stock_data)
    plt.figure(figsize=(10, 6))
    plt.plot(stock_data['Close'], label='Close Price')
    plt.plot(stock_data['Rolling Mean'], label='Rolling Mean (20 days)', color='red')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Close Price vs. Rolling Mean')
    plt.legend()
    st.pyplot(plt)

def main():
    st.title("Financial Data Retrieval and Analysis App")
    st.sidebar.header("Input Parameters")
    company_input = st.sidebar.text_input("Enter Company Ticker Symbol or Name", "AAPL")
    start_date = st.sidebar.date_input("Start Date", pd.Timestamp('2018-01-01'))
    end_date = st.sidebar.date_input("End Date", pd.Timestamp('2022-01-01'))
    if st.sidebar.button("Retrieve and Analyze Data"):
        try:
            ticker = yf.Ticker(company_input)
            symbol = ticker.info['symbol']
            company_name = ticker.info['longName']
            stock_data = fetch_financial_data(symbol, start_date, end_date)
            st.subheader(f"Stock Data for {company_name} ({symbol})")
            processed_data = process_data(stock_data)
            display_data(processed_data)
        except Exception as e:
            st.error(f"Error retrieving data: {e}")

if __name__ == "__main__":
    main()
