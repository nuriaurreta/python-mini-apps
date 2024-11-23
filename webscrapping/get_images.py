import requests
from bs4 import BeautifulSoup
import os

web_content = requests.get('https://www.jotdown.es/')

soup = BeautifulSoup(web_content.text, 'html.parser')
try:
    os.mkdir('images')
except:
    pass

for i, img in enumerate(soup.find_all('img')):
    src = img.get('src')
    extension = src.split('.')[-1]
    with open(f'images/img{i}.' + extension, 'wb')as file:
        res = requests.get(src)
        file.write(res.content)
