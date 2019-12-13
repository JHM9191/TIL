from flask import Flask, render_template, request
from decouple import config
import requests
app = Flask(__name__)

base = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    text = request.args.get('message')
    requests.get(f'{base}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    return render_template('send.html',text = text)


# 웹훅 
@app.route(f'/{token}', methods=['POST'])
def telegram():
    # Step 1: 구조 print 해보기 & 변수 저장
    # print(request.get_json())
    from_telegram = request.get_json()
    print(from_telegram)
    # Step 2: 그대로 돌려보내기
    if from_telegram.get('message') is not None: # NoneType일 경우만 예외처리
        chat_id = from_telegram.get('message').get('from').get('id')
        text = from_telegram.get('message').get('text')
        url = f'{base}/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
        requests.get(url)
    return '', 200