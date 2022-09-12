import requests
from bs4 import BeautifulSoup

URL = "https://www.listchallenges.com/100-random-foods"

r = requests.get(URL)
soup = BeautifulSoup(r.content, 'lxml')

lists = soup.find('div', attrs={'id': 'repeaterListItems'})
datas = lists.find_all('div', attrs={'class': 'item-name'})

foods = [data.text.strip() for data in datas]


