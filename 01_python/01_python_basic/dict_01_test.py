'''
Python dictionary 연습 문제
'''

# 1. 평균을 구하시오.
score = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')

sum = 0     # 미리 변수 선언 해줘야 함!
for value in score.values():        # 계산이 가능한 숫자형태로 가져오려면 .values()를 꼭 써줘야 함!
    sum += value                    # 그냥 score로 가져오게되면 데이터형 반영 안됨(?)

average = sum/len(score)
print(average)

# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 84,
        '국어': 90,
        '음악': 92
    },
    'b': {
        '수학': 83,
        '국어': 91,
        '음악': 77
    }
}


# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')

# averages = {'a반 평균':0, 'b반 평균':0}
# for value in scores['a'].values():
#     averages['a반 평균'] += value
# for value in scores['b'].values():
#     averages['b반 평균'] += value
# for value in averages:
#     value = value/3
# print(averages)

sum_score = 0
count = 0

for person_score in scores.values():
    # 여기에는 'a'와 'b' 에 대한 정보 들어옴
    for subject_score in person_score.values():
        # 여기에는 각 학생의 과목 점수에 대한 정보 들어옴
        sum_score += subject_score
        count += 1  # 과목 개수
result = sum_score/count
print(result)


# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?
print('==== Q3-1 ====')

for key, value in city.items():
    temps = 0
    for tag in value:   # [-6, -10, 5] 안의 tag들
        temps += tag
    temp = temps / len(value)
    print(f'{key}: {temp}')

# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?
print('==== Q3-2 ====')

count = 0
for key, value in city.items():
    if count == 0:
        hot_temp = max(value)
        cold_temp = min(value)
        hot_city = key
        cold_city = key
        count += 1
    else :
        if max(value) > hot_temp:
            hot_temp = max(value)
            hot_city = key
        if min(value) < cold_temp:
            cold_temp = min(value)
            cold_city = key
    
print(f'최근 3일 중 가장 추웠던 곳은 {cold_city}({cold_temp}도) 였고, 가장 따뜻한 곳은 {hot_city}({hot_temp}도) 였다.')

# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?
print('==== Q3-3 ====')
if 2 in city['서울']:
    print('서울은 영상 2도였던 적이 있습니다.')
else:
    print('서울은 영상 2도였던 적이 없습니다.')

# 아래에 코드를 작성해 주세요.