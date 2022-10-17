## Vietnamese Sentiment Analysis


### Introduction
Sentiment analysis is the process of analyzing online pieces of writing to determine the emotional tone they carry, whether they are **positive**, **negative**, or **neutral**. In simple words, sentiment analysis helps to find the author’s attitude towards a topic.
<p align='middle'><img src='./assets/sentiment.png' width=100% /></p>

This project aims to analyse the sentiments of vietnamese food comments crawled from [Foody](https://www.foody.vn/) along with their ratings. Since the rating range is from 0 to 10, I proceeded to reassign the value according to the following rules:
| Sentiment     | Condition            |
| ------------- | -------------------- |
| Negative      | (rating < 4) or NaN  |
| Neutral       | 4 ≤ rating ≤ 7       |
| Positive      | rating > 7           |

The training process is done on [Colab](https://drive.google.com/drive/folders/1RrUjuS0tffVOgOCqgP6BVhPvayzOPOH7?usp=sharing).


### How to use
* Step 1: Automatically install all dependencies from `requirements.txt`.
    ```
    pip install -r requirements.txt
    ```
* Step 2: Configure hyper-parameters in `config.py`.
* Step 3: Start server.
    ```
    python app.py
    ```
<p align='middle'><img src='./assets/homepage.png' width=100% /></p>