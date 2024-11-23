import requests
from bs4 import BeautifulSoup

web_content = requests.get('https://www.jotdown.es/')
soup = BeautifulSoup(web_content.text, 'html.parser')
search = soup.find_all('h3', class_="entry-title")

articles = {}

def show_titles():
    for i, element in enumerate(search):
        title = element.a.get('title')
        articles[i]=element.a.get('href')
        print(f'{i}: ' + title)

show_titles()

art = int(input('Which article do you want to read?'))

content = requests.get(articles[art])
art_soup = BeautifulSoup(content.text, 'html.parser')
search_content = art_soup.select_one(".entry-content")

print(search_content.get_text())

x = input('Read another one? (y/n)')

if x == 'y':
    show_titles()
    art = int(input('Which article do you want to read?'))
else:
    pass
