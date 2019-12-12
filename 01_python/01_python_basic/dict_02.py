import random

t4ir_6th = {
    'division': ['머신러닝', '빅데이터', 'IoT', 'VR'],
    'language': {
        'python': {
            'python standard library': ['os', 'random', 'webbrowser'],
            'frameworks': {
                'flask': 'micro',
                'django': 'full-functioning'
            },
            'data_science': ['numpy', 'pandas', 'scipy', 'sklearn'],
            'scraping': ['requests', 'bs4'],
        },
        'web' : ['HTML', 'CSS']
    },
    'classes': {
        '1305': {
            'lecturer': 'justin',
            'manager': '문주영',
            'class president': '문한나',
            'groups': {
                'A': ['문한나', '박나영', '김연주'],
                'B': ['백대현', '김완규', '윤동현'],
                'C': ['장민재', '강현수', '강동욱', '장하림'],
                'D': ['이 슬', '최희은', '전국현', '한상윤'],
                'E': ['최여진', '조현민', '김나윤', '유한솔']
            }
        },
        '503': {
            'lecturer': 'change',
            'manager': '신윤미'
        }
    }
}


"""
난이도* 1. 반 분류(division)는 몇 개 있나요?
출력예시)
4
"""
print("==== Q1 ====")
count = len(t4ir_6th['division'])
print(f'{count}개')

"""
난이도** 2. python standard library에 'requests'가 있나요?
출력예시)
False
"""
print("==== Q2 ====")
if 'requests' in t4ir_6th['language']['python']['python standard library']:
    print("True")
else :
    print("False")

"""
난이도** 3. 1305호의 반장의 이름을 출력하세요.
출력예시)
문한나
"""
print("==== Q3 ====")
president = t4ir_6th['classes']['1305']['class president']
print(president)

"""
난이도*** 4. t4ir에서 배우는 언어들을 출력하세요.
출력 예시)
python
web
"""

print("==== Q4 ====")
for key in t4ir_6th['language'].keys():
    print(key)

"""
난이도*** 5 t4ir 503호의 강사와 매니저의 이름을 출력하세요.
출력 예시)
change
신윤미
"""
print("==== Q5 ====")
for value in t4ir_6th['classes']['503'].values():
    print(value)

"""
난이도***** 6. framework 들의 이름과 설명을 다음과 같이 출력하세요.
출력 예시)
flask는 micro이다.
django는 full-functioning이다.
"""
print("==== Q6 ====")
for key, value in t4ir_6th['language']['python']['frameworks'].items():
    print(f'{key}는 {value}이다')

"""
난이도***** 7. 오늘 당번을 뽑기 위해 groups의 E 그룹에서 한명을 랜덤으로 뽑아주세요.
출력예시)
오늘의 당번은 최여진
"""
print("==== Q7 ====")
print(random.choice(t4ir_6th['classes']['1305']['groups']['E']))

