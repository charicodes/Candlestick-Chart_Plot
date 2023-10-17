import yfinance as yf
import mplfinance as mpf
import pandas as pd

# Define stock symbol and stock range
symbol = input("Enter Stock Name: ")
start_date = '2022-01-01'
end_date = '2023-10-16'

try:
    # Fetch stock data
    stock_data = yf.download(symbol, start=start_date, end=end_date)

    # Convert the index to DatetimeIndex
    stock_data.index = pd.to_datetime(stock_data.index)

    # Create the candlestick chart
    mpf.plot(stock_data, type='candle', style='yahoo', title=f'{symbol} Candlestick Chart')
except Exception as e:
    print(f"An error occurred: {str(e)}")

