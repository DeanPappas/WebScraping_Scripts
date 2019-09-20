'''
https://dev.to/ayushsharma/a-guide-to-web-scraping-in-python-using-beautifulsoup-1kgo
https://www.youtube.com/watch?v=aIPqt-OdmS0

'''
import requests
from bs4 import BeautifulSoup
import smtplib
import time

user = input("Enter a user: ")
tweetNum = int(input("Which tweet would you like to see: "))

URL1 = ("https://twitter.com/%s" % user)
headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
page = requests.get(URL1, headers = headers)
soup = BeautifulSoup(page.content, "html.parser")

href = soup.find_all(class_="ProfileHeaderCard")
profileNumbers = soup.find_all(class_="ProfileNav-value")
profileHeader = href[0].get_text().replace("\n"," ")
tweets = []

timeline = soup.select("#timeline li.stream-item")
for tweet in timeline:
	tweet_text = tweet.select("p.tweet-text")[0].get_text()
	tweets.append(tweet_text)

followers = int(profileNumbers[2].get_text())
following = int(profileNumbers[1].get_text())
ratio = float(followers/following)

print("")
print(user, "'s Account Overview\n")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Bio:", profileHeader[profileHeader.find("@")+(len(user)+4):-41])
print("Total tweets:", profileNumbers[0].get_text().rstrip())
print("Follwing:", profileNumbers[1].get_text())
print("Follwers:", profileNumbers[2].get_text())
print("%s's followers to following ratio is: %.2f" % (user, ratio))
print("Selected Tweet: ", tweets[tweetNum])
'''
print("Selected Tweets:\n")
for x in tweets:
	print(x, "\n")
'''
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")



