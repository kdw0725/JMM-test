import urllib.request
import requests
from bs4 import BeautifulSoup
import json


def loc():
    client_id = "fechS4lsKMLVwarW0I01"
    client_secret = "MxwdD119Rv"

    location = input("현재 위치를 알려주세요 : ")
    encText = urllib.parse.quote(location)

    url = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=' +encText+'&oquery='+encText+'&tqi=TItWDspVuEKssvZQOZZssssstq4-315036'

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if (rescode == 200):
        response_body = response.read()
        print(response_body.decode('utf-8'))
    else:
        print("Error Code:" + response)

def getGPS():
    client_id = "fechS4lsKMLVwarW0I01"
    client_secret = "MxwdD119Rv"
    location = input("현재 위치를 말씀해 주세요 : ")
    encText = urllib.parse.quote(location)

    url = 'https://openapi.naver.com/v1/search/local?query='+encText
    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()


    if (rescode == 200):
        response_body = response.read()
        locinfo = response_body.decode('utf-8')
        for item in locinfo.items():
            print(item)
    else:
        print("Error Code:" + response)
def find_info(search_url):
    res = requests.get(search_url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'html.parser')

    section_sname = soup.find("h2", {"class" : "tit_location"})
    section_pnum = soup.find("span", {"class" : "txt_contact"})
    section_addr = soup.find("span", {"class" : "txt_address"})

    for name in section_sname:
        print(name)
    for pnum in section_pnum:
        print(pnum)
    for addr in section_addr:
        print(addr)


def search_info():
    location = input("맛집 이름 입력 : ")
    encText = urllib.parse.quote(location)
    search_url = 'https://search.daum.net/search?w=tot&DA=YZR&t__nil_searchbox=btn&sug=&sugo=&q='+encText

    html = requests.get(search_url).text
    soup = BeautifulSoup(html,'html.parser')
    maps = soup.findAll('div',{'class':"wrap_place"})
    for b in maps:
        for link in b.findAll('a'):
            if 'href' in link.attrs:
                if 'place' in link.attrs['href']:
                    find_info(link.attrs['href'])

if __name__ == '__main__':
    getGPS()