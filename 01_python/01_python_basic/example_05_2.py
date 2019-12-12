import webbrowser
import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = 'https://www.naver.com'
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')
now = datetime.now()    # 현재 시간을 담아줌

##### 실시간 검색어 순위 크롤링 #####
    #여러 개를 뽑아오기 때문에 select_one 아니라 select 사용!
search = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul > li .ah_k')  # li 안에 있는 모든 ah_k 뽑아옴
#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5) > li:nth-child(1) > a > span.ah_k
#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(5) > li.ah_item.ah_on > a > span.ah_k

print(f'{now} 기준 실시간 검색어') # f string - 변화하는 변수와 스트링을 같이 출력할 때 사용!

# for name in search:
#     print(name.text)

for i, name in enumerate(search):
    print(f'{i+1}위: {name.text}')
