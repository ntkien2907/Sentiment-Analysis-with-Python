from flask import Flask, request, render_template
from tensorflow.keras.models import load_model
from config import *

app = Flask(__name__)
model = load_model(CLS_MODEL)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def receive_text():
    text = request.form['text']
    sentiment = predict_sentiment(text)
    return render_template('index.html', sentiment=sentiment, text=text)

def predict_sentiment(text):
    if text != '':
        if NN_ARCHITECTURE == 'cnn':
            from cnn import CNN_predict
            return CNN_predict(text, model)
        elif NN_ARCHITECTURE == 'lstm-cnn':
            from lstm_cnn import LSTM_CNN_predict
            return LSTM_CNN_predict(text, model)
    return -1

if __name__ == "__main__":
    app.run(host=HOST, port=PORT)