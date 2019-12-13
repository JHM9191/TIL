from flask import Flask, render_template, request
from datetime import datetime
import random
app = Flask(__name__)

@app.route('/')
def hello():
    # return "Hello World!"
    return render_template('index.html')

# if __name__ == "__main__":
#     app.run()

@app.route('/t4ir')
def t4ir():
    return 'This is T4IR'

@app.route('/ssafy')
def ssafy():
    return 'SAFFY'

@app.route('/ssafy2')
def ssafy2():
    return 'SAFFY2'

@app.route('/ssafy3')
def ssafy3():
    return 'SAFFY3'


@app.route('/dday')
def dday():
    today = datetime.now()
    end = datetime(2020, 4, 21)
    td = end - today
    # print(dir(td))
    print(dir(today))
    return f'오늘은 {today.year}년 {today.month}월 {today.day}일 입니다.\n\n 과정은 {end.year}년 {end.month}월 {end.day}에 끝납니다. 현재 {td.days}일 남았습니다.'
    
    # return f'{td.strftime("%Y")}년 {td.strftime("%b")}월 {td.days}일 남았습니다.'

    
@app.route('/html')
def html():
    return '<h1>This is HTML h1 tag!</h1>'
    
@app.route('/html_line')
def html_line():
    return """
    <h1>여러줄을 보내봅시다.</h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>
    """

@app.route('/greeting/<name>')
def greeting(name):
    # return f'반갑습니다! {name}님!'
    return render_template('greeting.html',html_name=name)

@app.route('/cube/<int:number>')
def cube(number):
    # return f'{number}의 3제곱은 {number**3}입니다.'
    result = number**3
    return render_template("cube.html", result=result, number=number)


@app.route('/lunch/<int:people>')
def lunch(people):
    menu = ['짜장면', '짬뽕', '볶음밤', '고추잡채밥','마파두부']
    order = random.sample(menu, people)
    return str(order)

@app.route('/movie')
def movie():
    movies = ['겨울왕국2','머니게임','왕좌의게임']
    return render_template('movie.html', movies=movies)

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    age = request.args.get('age')
    return render_template('pong.html', age_in_html = age)
    
@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/google')
def google():
    return render_template('google.html')

@app.route('/isityourbirthdaytoday')
def birthday():
    today = datetime.now()
    if today.month == 11 and today.day == 1:
        result = True
    else:
        result = False
    
    return render_template('birthday.html', result = result)

@app.route('/vonvon')
def vonvon():
    return render_template('vonvon.html')

@app.route('/godmademe')
def godmademe():
    name = request.args.get('name')
    first_list = ['잘생김','못생김','어중간']
    second_list = ['자신감','쑥스러움','애교','잘난척']
    third_list = ['허세','돈복','식욕','물욕','성욕']
    first = random.choice(first_list)
    second = random.choice(second_list)
    third = random.choice(third_list)
    return render_template('godmademe.html', name = name, first = first, second = second, third = third)


# 서버를 다시 시작하지 않아도 수정된 사항이 반영될 수 있도록. 
if __name__=='__main__':
    app.run(debug=True)