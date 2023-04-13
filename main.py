import requests
from bs4 import BeautifulSoup
from inflection import titleize


def titles_generator(links):
    titles = []

    def post_formatter(url):
        if 'posts' in url:
            url = url.split('/')[-1]
            url = url.replace('-', ' ')
            url = titleize(url)
            titles.append(url)


    for link in links:
        if link.get('href') == None:
            continue
        else:
            post_formatter(link.get('href'))

    return titles

r = requests.get('http://www.dailysmarty.com/topics/python')
soup = BeautifulSoup(r.text, 'html.parser')
links = soup.findAll('a')
titles = titles_generator(links)

for title in titles:
    print(title)