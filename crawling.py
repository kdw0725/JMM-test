import urllib.request
import requests
from bs4 import BeautifulSoup
import json
import datetime
import re

def menuCraw():
    dt = datetime.datetime.now()
    today_week = dt.weekday()
    url = 'http://skhu.ac.kr/uni_zelkova/uni_zelkova_4_3_view.aspx?idx=349&curpage=1'
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, 'html.parser')
    lunch_menu = soup.find_all("td", {"class" : "color606"})
    a = lunch_menu[today_week]
    b = str(a).split('<br/>')

    print(b)


def userGPS():
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
        json_data = json.loads(locinfo)
        item = json_data.get('items')
        posx = item[0].get('mapx')
        posy = item[0].get('mapy')
        print(location+"의 GSP 주소는 ("+posx+","+posy+")입니다.")

    else:
        print("Error Code:" + response)

def storeInfo():
    client_id = "fechS4lsKMLVwarW0I01"
    client_secret = "MxwdD119Rv"
    location = input("가게 이름 : ")
    encText = urllib.parse.quote(location)

    store_url = 'https://openapi.naver.com/v1/search/local?query='+encText
    request = urllib.request.Request(store_url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if(rescode ==200):
        response_body = response.read()
        locinfo = response_body.decode('utf-8')

        json_data = json.loads(locinfo)
        item = json_data.get('items')

        s_title = item[0].get('title')
        s_telephone = item[0].get('telephone')
        s_address = item[0].get('address')
        s_roadAddress = item[0].get('roadAddress')
        s_mapx = item[0].get('mapx')
        s_mapy = item[0].get('mapy')
        store_information = [s_title, s_telephone, s_address, s_roadAddress, s_mapy, s_mapx]
        for i in store_information:
            print(i)
    else:
        print("Error Code:"+response)

if __name__ == '__main__':
    storeInfo()
    'https://github.com/s-owl/skhufeeds/blob/master/skhufeeds/crawlers/crawlers/menu.py'
