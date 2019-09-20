'''
Sales checker for switch games on my wishlist using bs4 and requests
Separated by comments with each games title
Checks for class_ = "sale-price"
'''

import requests
from bs4 import BeautifulSoup
import smtplib
import time
from selenium import webdriver

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

# DEADBOLT
deadbolt = "https://www.nintendo.com/games/detail/deadbolt-switch/"

page1 = requests.get(deadbolt, headers = headers)
soup1 = BeautifulSoup(page1.content, "html.parser")

title = soup1.find(class_ = "title").get_text().strip().rstrip("\nNintendo Switch")
price = soup1.find(class_ = "msrp").get_text().strip()
sale = soup1.find("div", {"class": "price discounted loaded"})

print("Game:", title)
print("Price:", price)
print(sale)


# BEAT COP
beatcop = "https://www.nintendo.com/games/detail/beat-cop-switch/"



headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
page2 = requests.get(beatcop, headers = headers)
soup2 = BeautifulSoup(page2.content, "html.parser")

title = soup2.find(class_ = "title").get_text().strip().rstrip("\nNintendo Switch")
price = soup2.find(class_ = "msrp").get_text().strip()
#sale = soup2.find(class_ = "price discounted loaded")
sale = soup2.find("div", {"class": "discounted"})

print("Game:", title)
print("Price:", price)
print(sale)
if soup2.find("div", {"class": "discounted"}) is not None:
    print("Tag Found")