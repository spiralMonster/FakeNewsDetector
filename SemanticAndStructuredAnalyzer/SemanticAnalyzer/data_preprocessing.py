import numpy as np
import pandas as pd
import re
import string
import json
from tensorflow.keras.preprocessing.sequence import pad_sequences


def process_text(text):
    with open("../Models/stopwords.json") as file:
        stopwords=json.load(file)
    ## Removing urls from text:
    text = re.sub(r'((http|https)://)?(www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(/[a-zA-Z0-9#./?=&%+-]*)?', '', text)

    ## Removing twitter urls from text:
    text = re.sub(r'pic.twitter.com/[a-zA-Z0-9]+', '', text)

    ## Removing more than one blank spaces:
    text = re.sub(r'\s{2,}', ' ', text)

    ## removing punctuation marks in the text:
    punc_table = str.maketrans('', '', string.punctuation)

    ## removing numeric values attached with text"
    num_table = str.maketrans('', '', '0123456789')

    list_words = text.split(" ")
    final_text = ""
    for word in list_words:
        word = word.translate(punc_table)
        word = word.translate(num_table)
        word = word.lower()
        if word.isalpha():
            if word not in stopwords:
                final_text += word
                final_text += " "

    final_text = final_text.strip()
    return final_text


def DataPreprocessing(posted_article:str,tokenizer):
    processed_text=process_text(posted_article)
    tokenized_text=tokenizer.texts_to_sequences([processed_text])
    padded_text=pad_sequences(tokenized_text,maxlen=300,padding="post",truncating="post")
    print("Data preprocessing completed...")
    return padded_text
