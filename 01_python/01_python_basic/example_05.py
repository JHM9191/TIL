import webbrowser
import requests
from bs4 import BeautifulSoup

# res = requests.get('http://www.daum.net')
# response = requests.get('http://www.daum.net').text
# print(res.status_code)

url = 'https://finance.naver.com/sise/'
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')
kospi = soup.select_one('#KOSPI_now')
print(kospi.text)