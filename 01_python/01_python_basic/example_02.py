import webbrowser
import requests
from bs4 import BeautifulSoup
from datetime import datetime

# webbrowswer 사용해보기

# webbrowser.open('www.google.co.kr') # 새로운 탭 열림
# webbrowser.open_new('www.naver.com') # 새로운 탭 열림
# webbrowser.open_new_tab('www.daum.net') # 새로운 탭 열림

# webbrowser.open_new_tab('http://70.12.113.219/sp365/main.sp') # 새로운 탭 열림


# requests 실습
# response = requests.get('http://naver.com')
#http://naver.com 안에 있는 모든 텍스트를 가져온다. 
# print(response.text)
# print(response.status_code)

# url = 'https://finance.naver.com/sise/'
# res = requests.get(url).text
# soup = BeautifulSoup(res, 'html.parser')
# kospi = soup.select_one('#KOSPI_now')
# print(kospi.text)


# url = 'https://finance.naver.com/marketindex/'
# res = requests.get(url).text
# soup = BeautifulSoup(res, 'html.parser')
# wondollar = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value')
# yendollar = soup.select_one('#worldExchangeList > li.on > a.head.jpy_usd > div > span.value')
# print(wondollar.text)
# print(yendollar.text)


url = 'https://www.naver.com/'
res = requests.get(url).text
soup = BeautifulSoup(res, 'html.parser')
#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li:nth-child(17) > a > span.ah_k
#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li .ah_k
keyword = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li .ah_k')

now = datetime.now()
print(f'{now}기준 실기간 검색어')
# for name in keyword:
#     print(name.text)

for i, name in enumerate(keyword):
    print(f'{i + 1}위: {name.text}')    