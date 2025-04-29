# Used Google Finance for extracting real-time stock data

# Import required libraries
import requests  # For making HTTP requests
from bs4 import BeautifulSoup  # For parsing and extracting data from HTML
import time  # For introducing delay between requests

# Set the stock details
ticker = 'INFY'      # Ticker: Change the stock ticker symbol as per your requirement
exchange = 'NSE'     # Stock Exchange: Change according to the exchange (e.g., NSE, BSE, NASDAQ)

# Construct the URL for fetching stock data from Google Finance
url = f'https://www.google.com/finance/quote/{ticker}:{exchange}'

# Loop to fetch and display stock price multiple times
for i in range(10):  # Number of times to fetch the price; increase for more instances
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Class name used by Google Finance for displaying the current stock price
        class1 = 'YMlKec fxKbKc'

        # Extract the stock price, remove unwanted characters, and convert to float
        price = float(soup.find(class_=class1).text.strip()[1:].replace(",", ""))

        # Print the extracted stock price
        print(f"{ticker} ({exchange}): {price}")

    except Exception as e:
        # Handle any potential errors (e.g., connection issues, parsing errors)
        print(f"Error fetching stock data: {e}")

    # Wait for 10 seconds before making the next request (adjustable)
    time.sleep(10)
