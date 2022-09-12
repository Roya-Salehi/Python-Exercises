import requests
from bs4 import BeautifulSoup

url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
articles = soup.find_all(class_="paywall")
article = '\n'.join([p.text for p in articles])
print(article)