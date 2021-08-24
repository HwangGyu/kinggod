import enum
from flask import Flask, redirect, render_template, request
import json

from werkzeug.utils import append_slash_redirect

app = Flask(__name__)
pw = 'awdawdasdasawdadawdadwawdwad'

question = [
    '요즘 갈증이 나서 물을 많이 마신다',
    '소변량이 늘어 화장실을 자주 간다',
    '최근에 체중이 갑자기 빠졌다',
    '눈의 초점이 잘 안 잡히는 증상이 나타난다',
    '잇몸염증이 자주 발생하고 피가 난다',
    '목이 자주 마르고 소변량이 늘어나며 항상 배가 고프다',
    '아무런 이유 없이 살이 빠지고 항상 무기력하다',
    '운동을 거의 하지 않는다',
    '아무런 이유 없이 살이 빠지고 항상 무기력하다',
    '스트레스를 많이 받는다',
    '부스럼이 잘 일어나고 가려움증이 심하다',
    '눈에 초점이 잘 안잡힌다',
    '항상 나른하고 매사가 귀찮다',
    '다리에 쥐가 자주 난다.',
    '손발톱이 약해지고 빠지거나 갈라지는 일이 많다.',
    '갑자기 비염에 걸리기도 하고 피부가 가려운 일이 잦다.',
    '평소 체온이 평균 체온보다 낮다.',
    '걸핏하면 입안에 염증이 생긴다.',
    '많은 약을 먹고 있다.',
    '목이 마를 때가 많다.',
    '입맛이 바뀌었다는 말을 종종 듣는다.',
    '예전만큼 술을 마시지 못한다(학생 체크 X)',
    '빈혈 증세를 가끔 느낀다.',
    '몸이 차가울 때가 많다.',
    '스트레스는 느끼지 않지만, 휴일에도 가만히 있지를 못한다.',
    '잠들기가 힘들고 자려고 하면 눈이 말똥말똥해진다.',
    '저녁형 인간이라 밤 늦게까지 깨어 있다.',
    '식사를 빨리 하는 편이다.',
    '설탕이 들어간 칸커피나 청량음료를 자주 마신다.',
    '채소 요리를 그다지 즐겨 먹지 않는다.',
    '가공한 채소나 냉동 식품,레토르트식품을 자주 먹는다.'


]

q_len = len(question)
print(q_len)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/main')
def f1():
    return render_template('main.html', lenawd=q_len, question = question, enumerate=enumerate)

if __name__ == "__main__":
    app.run('0.0.0.0', port=80, debug=True)
