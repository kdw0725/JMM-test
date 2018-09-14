import requests                     #웹 상 데이터 처리 모듈
from bs4 import BeautifulSoup       #가독성을 높혀주는 모듈

URL = 'https://www.google.co.kr/search?q=%EC%85%B0%EC%85%B0&oq=%EC%85%B0%EC%85%B0&aqs=chrome..69i57j0l5.3024j0j8&sourceid=chrome&ie=UTF-8&npsic=0&rflfq=1&rlha=0&rllag=37518232,126748089,7505&tbm=lcl&rldimm=8297771894564145484&ved=2ahUKEwjc-4PTgKjdAhVHfrwKHfNsBwMQvS4wAXoECAEQCQ&rldoc=1&tbs=lrf:!3sIAE,lf:1,lf_ui:2&rlst=f'

response = requests.get(URL)

html = response.text

print(html)

python