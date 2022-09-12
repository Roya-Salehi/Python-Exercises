import requests
from bs4 import BeautifulSoup

url = 'http://www.nytimes.com/'
response = requests.get(url)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
titles = soup.find_all(class_='indicate-hover')
listoftitles = [t.text for t in titles]
fname = input("Enter file name: ")
with open(f'./assets/{fname}.txt', 'w') as textfile:
    for title in listoftitles:
        textfile.write(title + '\n')
