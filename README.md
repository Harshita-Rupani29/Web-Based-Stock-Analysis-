
---

Financial Data Retrieval and Analysis App

This is a Streamlit-based web application that retrieves and analyzes financial stock data. The app allows users to fetch historical stock prices and visualize key trends like the rolling mean of the stock's closing prices.

Features

Input any stock ticker symbol or company name.

Select a date range for historical stock data.

Automatically fetch stock data from Yahoo Finance.

Calculate and display the 20-day rolling mean for the stock's closing price.

Visualize the stock's closing price and rolling mean with interactive plots.


Installation

1. Clone this repository or copy the Python script to your local machine.


2. Make sure you have Python 3.8 or later installed.


3. Install the required dependencies by running:

pip install streamlit yfinance pandas matplotlib



Usage

1. Run the Streamlit app by executing the following command:

streamlit run <script_name>.py

Replace <script_name>.py with the name of the Python script (e.g., app.py).


2. Open the app in your browser at http://localhost:8501 or the URL provided by Streamlit.


3. Enter the required inputs:

Company Ticker Symbol or Name: Enter the ticker symbol (e.g., AAPL for Apple).

Start Date: Select the start date for the analysis.

End Date: Select the end date for the analysis.



4. Click the "Retrieve and Analyze Data" button to fetch and analyze the stock data.



File Structure

fetch_financial_data(symbol, start_date, end_date): Fetches historical stock data from Yahoo Finance.

process_data(stock_data): Adds a 20-day rolling mean column to the dataset.

display_data(stock_data): Displays the processed data and visualizes it with Matplotlib.


Dependencies

Streamlit - Interactive web framework for Python.

yfinance - Yahoo Finance API wrapper.

Pandas - Data manipulation library.

Matplotlib - Plotting library.


Example Output

Processed Stock Data Table: Displays the stock prices and calculated rolling mean.

Interactive Plot: Shows the stock's closing price and rolling mean for the selected date range.


Error Handling

The app includes basic error handling to manage issues like invalid ticker symbols or unavailable stock data.

Contributing

If you'd like to contribute to this project, feel free to submit a pull request or open an issue.

License

This project is licensed under the MIT License. Feel free to use it as you see fit.


---
