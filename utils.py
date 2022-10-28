from tensorflow.keras.models import load_model
from config import *

sentiment_model = load_model(CLS_MODEL)

def predict_sentiment(text):
    if text != '':
        if NN_ARCHITECTURE == 'cnn':
            from cnn import CNN_predict
            return CNN_predict(text, sentiment_model)
        elif NN_ARCHITECTURE == 'lstm-cnn':
            from lstm_cnn import LSTM_CNN_predict
            return LSTM_CNN_predict(text, sentiment_model)
    return -1