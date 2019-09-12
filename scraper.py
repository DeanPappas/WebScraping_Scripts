import requests
from bs4 import BeautifulSoup
import smtplib

URL = "https://www.amazon.com/Wireless-Bluetooth-Audio-Technica-ATH-M50X-Headphones/dp/B07HNP7RZH"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

page = requests.get(URL, headers = headers)

soup = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup.prettify(), "html.parser")

title = soup2.find(id = "productTitle").get_text()
price = soup2.find(id = "priceblock_ourprice").get_text()
converted_price = float(price[1:6])

if converted_price < 39.95:
	send_email()
		
print(title.strip())
print(price.strip())

def send_email():
	
#https://www.youtube.com/watch?v=Bg9r_yLk7VY AT 11:13   pw: pyxd hxag lwvn dtni