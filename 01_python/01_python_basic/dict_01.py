# Dictionary 만드는 방법

# 1.
my_dict = {'한국어':'안녕', '영어':'hi', '독일어':'Geten tag'}

# 2.
my_dict2 = {}
my_dict2['한국어']='안녕'
my_dict2['영어']='hi'
my_dict2['독일어']='Geten tag'

# 3.
my_dict3 = dict(한국어 = '안녕', 영어 = 'hi', 독일어 = 'Geten tag')

print(my_dict)
print(my_dict2)
print(my_dict3)

#위 방법들을 섞어서 써도 됨!
area_code={'서울':'02'}
area_code['경기도'] = '031'
print(area_code)

for key in area_code:
    print(key)              # 키 값 출력
    print(area_code[key])   # 키 값에 해당하는 value 값 출력


for key, value in area_code.items():    #키와 value를 한번에 다 뽑고 싶을 때는 .items() 붙여야 함!
    print(key, value)


for value in area_code:        #value값만 뽑아내고 싶을 때는 .values() 붙어야 함!
    print(value)
