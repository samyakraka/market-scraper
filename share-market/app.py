# Used Google Finance for extracting real-time stock data 
import requests
from bs4 import BeautifulSoup
import time

ticker = 'LICI'  # Ticker: Change Stock Name according to your choice just google it once which and check the ticker name of the Stock
exchange = 'NSE'  # Stock Exhange: Change Stock Exchange in which your stock belongs tp
url = f'https://www.google.com/finance/quote/{ticker}:{exchange}'

for i in range(10): # For only 10 instaces it will give the output if you want more then increase it
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    class1 = 'YMlKec fxKbKc'
    price = float(soup.find(class_=class1).text.strip()[1:].replace(",", ""))
    print(price)
    time.sleep(10) # If you want the change the duration of time you can 
