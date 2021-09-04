from flask import Flask, redirect, render_template, request
import json
import tensorflow as tf
from tensorflow.keras import *
import numpy as np
from tensorflow.keras.utils import to_categorical 

app = Flask(__name__)
pw = 'awdawdasdasawdadawdadwawdwad'

def init():
    global md
    md = models.load_model('diabets.h5')
    print("Model loaded!")


def preprocess(arr):
    data = np.array(arr)
    data = np.reshape(data, (-1, 8))
    return data


@app.route('/')
def main():
    return render_template('main.html')
@app.route('/index.html')
def awd():
    return render_template('index.html')
@app.route('/submit', methods=['POST'])
def output():
    print('Get Value')
    a = float(request.form['Pregnancies'])
    b = float(request.form['Glucose'])
    c = float(request.form['BloodPressure'])
    d = float(request.form['SkinThickness'])
    e = float(request.form['Insulin'])
    f = float(request.form['BMI'])
    g = float(request.form['DiabetesPedigreeFunction'])
    h = float(request.form['Age'])

    print('Preprocessing')
    Xdata = [a, b, c, d, e, f, g, h]
    Xdata = preprocess(Xdata)

    print('Predict')
    res = md.predict(Xdata).tolist()

    out = json.dumps({'1':res[0][0], '2':res[0][1]})
    return out



if __name__ == "__main__":
    init()
    app.run('0.0.0.0', port=80, debug=True)


