# спарсить сайт http://kenesh.kg/ru/news/all/list
# включая плагинацию 20 страниц
# img, date, title
# сохранить в csv
# загрузить проект на github

import requests
from bs4 import BeautifulSoup
import csv

def write_csv(data):
    with open('kenesh.csv','a') as f:
        writer = csv.writer(f)
        writer.writerow([data['title'],data['date'],data['image']])
def get_html(url):
    response = requests.get(url)
    return response.text
for i in range(20):
    url = f'http://kenesh.kg/ru/news/all/list?page={i+1}'
    access = get_html(url)
    page = BeautifulSoup(access,'lxml')
    news = page.find_all('div','news__item news__item__3')
    for i in news:
        title = i.find('a', class_ = 'news__item__title__link').text
        date = i.find('div', class_ = 'news__item__date').text
        image = 'https://kenesh.kg/' + i.find('img', class_='news__item__image__img').get('src')
        ls = {'title':title,'date': date,'image':image}
        write_csv(ls)# Parsing
