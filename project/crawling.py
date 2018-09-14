import requests
from bs4 import BeautifulSoup


page_url = 'https://store.naver.com/restaurants/detail?id=36470179'

res = requests.get(page_url)
res.raise_for_status()
soup = BeautifulSoup(res.text,'html.parser')


section_sname = soup.find("strong",{"class" : "name"})
section_addr = soup.find("span",{"class" : "addr"})
section_pnum = soup.find("div",{"class" : "txt"})

for name in section_sname:
    print(name)
for addr in section_addr:
    print(addr)
for pnum in section_pnum:
    print(pnum)


