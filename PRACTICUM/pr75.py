"""https://tortocake.com/

Скачайте 5 изображений тортов с указанного сайта.
(Для справки: в имени файла изображения должно быть "tort-")
"""

import requests
from bs4 import BeautifulSoup
import os

URL = 'https://tortocake.com/'

response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser')

images = soup.find_all('img')
torts_jpeg = []

for image in images:
    src = image.get('src')
    if src and 'tort-' in src:
        torts_jpeg.append(src)
        print(image.get('src'))

for tort in torts_jpeg:
    tort = URL + tort
    response = requests.get(tort)
    filename = tort.split('/')[-1]
    with open(filename, 'wb') as file:
        file.write(response.content)

