from flask import Flask, request, render_template
from utils import *

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def receive_text():
    text = request.form['text']
    sentiment = predict_sentiment(text)
    return render_template('index.html', sentiment=sentiment, text=text)

if __name__ == "__main__":
    app.run(host=HOST, port=PORT)