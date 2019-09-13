import requests
from bs4 import BeautifulSoup
import smtplib
import time

user = input("Enter a user: ")

URL1 = ("https://twitter.com/%s" % user)

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}

page = requests.get(URL1, headers = headers)

soup = BeautifulSoup(page.content, "html.parser")

profileNumbers = soup.find_all(class_="ProfileNav-value")


print("Total tweets:", profileNumbers[0].get_text().rstrip())
print("Follwing:", profileNumbers[1].get_text())
print("Follwers:", profileNumbers[2].get_text())

followers = int(profileNumbers[2].get_text())
following = int(profileNumbers[1].get_text())
ratio = float(followers/following)

print("%s's followers to following ratio is: %.2f" % (user, ratio))