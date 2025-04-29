# Import required libraries
import requests  # For sending HTTP requests
from bs4 import BeautifulSoup  # For parsing HTML content
import time  # For adding delay between requests

# Set the cryptocurrency and currency
coin = 'BTC'         # Cryptocurrency symbol (e.g., BTC for Bitcoin)
currency = 'INR'     # Display currency (e.g., INR for Indian Rupee)

# Construct the URL for fetching the cryptocurrency price from Google Finance
url = f'https://www.google.com/finance/quote/{coin}-{currency}'

# Fetch and display the price 10 times with a 10-second interval
for i in range(10):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Parse the HTML response using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Define the class name used by Google Finance for displaying the price
        class1 = 'YMlKec fxKbKc'

        # Extract the price string, clean it, and convert to float
        price = float(soup.find(class_=class1).text.strip().replace(",", "").replace("₹", ""))

        # Print the current price of the cryptocurrency
        print(f"{coin}-{currency}: {price}")

    except Exception as e:
        # Handle any errors (e.g., network issues or parsing errors)
        print(f"Error fetching data: {e}")

    # Wait for 10 seconds before making the next request
    time.sleep(10)
