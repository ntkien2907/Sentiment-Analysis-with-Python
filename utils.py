import string
import re
import numpy as np
import pandas as pd
from underthesea import word_tokenize
from gensim.models import Word2Vec
from tensorflow.keras.models import load_model
from config import *

## Preprocess data
df = pd.read_csv(ABBREVIATIONS_CSV, header=None)
abbreviations, meanings = np.array(df[0]), np.array(df[1])

def preprocess_sentence(text):
    # Convert string into lowercase
    text = text.lower()
    # Replace URL by <link_spam>
    text = re.sub(r"(?P<url>https?://[^\s]+)", "link_spam", text)
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Convert abbreviation into its meaning
    for abbreviation, meaning in zip(abbreviations, meanings):
        text = re.sub(rf"\b{abbreviation}\b", meaning, text)
    # Remove numbers
    text = re.sub(r"\d+", " ", text)
    # Tokenize sentence, remove word with only 1 character
    tokens = text.split()
    tokens = [token for token in tokens if len(token) > 1]
    # Concatenate tokens to sentence
    return ' '.join(tokens)

## Embed data
w2v_model = Word2Vec.load(W2V_MODEL)
vocab = w2v_model.wv.vocab.keys()
def embed_sentence(text):
    matrix = np.zeros((SEQUENCE_LENGTH, EMBEDDING_SIZE))
    tokens = word_tokenize(text)
    for i in range(SEQUENCE_LENGTH):
        idx = i % len(tokens)
        if tokens[idx] in vocab:
            matrix[i] = w2v_model.wv[tokens[idx]]
    matrix = np.array(matrix)
    return matrix

## Load sentiment model
sentiment_model = load_model(CLS_MODEL)

## Predict sentiment from text
def predict_sentiment(text):
    if text != '':
        return CNN_predict(text, sentiment_model)
    return -1

### CNN
def CNN_predict(text, model):
    text = preprocess_sentence(text)
    x = np.expand_dims(embed_sentence(text), axis=0)
    x = np.expand_dims(x, axis=3)
    result = model.predict(x)
    return np.argmax(result)