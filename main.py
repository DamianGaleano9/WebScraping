from bs4 import BeautifulSoup
import requests


url = 'http://www.dailysmarty.com/topics/python'

html_page = requests.get(url)
# result = html_page.text

soup = BeautifulSoup(html_page.text, 'html.parser')

post_items = soup.find_all('a')


for post in post_items:
    print(post.get('href'))
