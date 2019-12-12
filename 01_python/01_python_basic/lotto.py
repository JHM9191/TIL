import requests
import random
from bs4 import BeautifulSoup

# 888회 로또 api 데이터 가져오기

    ##둘이 이거 무슨 차이지? (json() / text로 받고 beautifulSoup)
response = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=888')
lotto = response.json()
print(lotto)

res = requests.get('https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=888').text
soup = BeautifulSoup(res, 'html.parser')
print(soup)

# 그 중에서 당첨번호 6개만 가져오기
luckynum = []
for i in range(1,7):
    luckynum.append(lotto[f'drwtNo{i}'])
print(luckynum)

# 랜덤으로 로또번호 생성하기
mynum = sorted(random.sample(range(1,46), 6))   ## sorted - 배열 오름차순 정렬
print(mynum)

# 실제 당첨번호와 랜덤으로 생성한 로또번호의 일치하는 정도에 따른 등수 표시하기
matched = 0
for num in mynum:
    if num in luckynum:
        matched +=1

if matched == 6:
    print('1등입니다')
elif matched == 5:
    print('2등입니다')
elif matched == 4:
    print('3등입니다')
elif matched == 3:
    print('4등입니다')
elif matched == 2:
    print('5등입니다')
elif matched == 1:
    print('6등입니다')
else:
    print('당첨되지 않았습니다')


# 1등 당첨되기 위해서 구입해야 하는 로또 갯수 구하기

while matched < 5:
    mynum = sorted(random.sample(range(1,46), 6)) 
    print(mynum)
    matched = 0
    for num in mynum:
        if num in luckynum:
           matched +=1
           
    if matched == 6:
        print('1등입니다')
    elif matched == 5:
        if(lotto['bnusNo']) in mynum:
            print('2등입니다')
        else:
            print('3등입니다')
    elif matched == 4:
        print('4등입니다')
    elif matched == 3:
        print('5등입니다') 
    else:
        print('당첨되지 않았습니다')