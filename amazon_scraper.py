import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = "https://www.amazon.com/Wireless-Bluetooth-Audio-Technica-ATH-M50X-Headphones/dp/B07HNP7RZH"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

page = requests.get(URL, headers = headers)

soup = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup.prettify(), "html.parser")

title = soup2.find(id = "productTitle").get_text()
price = soup2.find(id = "priceblock_ourprice").get_text()
converted_price = float(price[1:6])

print(title.strip())
print(price.strip())

def check_price():
	if converted_price < 39.95:
		send_email()
	else:
		print("No Sale")
		

def send_email():
	server = smtplib.SMTP("smtp.gmail.com", 587)
	server.ehlo()
	server.starttls()
	server.ehlo()
	
	server.login("kpappas302@gmail.com", "pyxdhxaglwvndtni")
	
	subject = "~AudioTechnica BT Adapter Price Drop~"
	body = "https://www.amazon.com/Wireless-Bluetooth-Audio-Technica-ATH-M50X-Headphones/dp/B07HNP7RZH"
	
	msg = ("Subject: %s\n\n%s") % (subject, body)
	
	server.sendmail("kpappas302@gmail.com","kpappas302@gmail.com",msg)
	print("EMAIL SENT")
	
	server.quit()
	
while(True):	
	check_price()
	time.sleep(10800)
	
#https://www.youtube.com/watch?v=Bg9r_yLk7VY 