import numpy as np
import pandas as pd
from spellchecker import SpellChecker
import re
import string


def check_single_quote_error(text: str):
    num_errors = 0
    list_words = text.split(" ")
    ind1 = 0

    while ind1 < len(list_words) - 1:
        ind2 = ind1 + 1
        word1 = list_words[ind1]
        word2 = list_words[ind2]

        if word1.isalpha() and word2.isalpha():
            word1 = word1.lower()
            word2 = word2.lower()

            if len(word1) > 1 and len(word2) == 1:
                if (word2) not in ['a', 'i']:
                    num_errors += 1

            elif word1 == "i" and word2 == "ll":
                num_errors += 1

        ind1 += 1

    return num_errors


def check_spacing_error(text: str):
    num_errors = 0
    list_words = text.split(" ")

    for word in list_words:
        if word == "":
            num_errors += 1

    return num_errors


def check_social_media_handle(text: str):
    num_handles = 0
    list_words = text.split(" ")

    for word in list_words:
        if "@" in word:
            num_handles += 1

    return num_handles


def check_urls(text: str):
    pattern = r'https?://\S+'
    matches = re.findall(pattern, text)
    return len(matches)


def check_twitter_post_urls(text:str):
    pattern=r'pic.twitter.com/\S+'
    matches=re.findall(pattern,text)
    return len(matches)


def check_hastags(text:str):
    pattern=r'#\S+'
    matches=re.findall(pattern,text)
    return len(matches)


def check_space_absence_after_sentence_completion(text: str):
    num_errors = 0
    list_words = text.split(" ")

    for word in list_words:
        if "." in word:
            if "." != word[-1]:
                num_errors += 1

    return num_errors


def check_capatalized_words(text: str):
    table = str.maketrans("", "", string.punctuation)
    num_capitalized_words = 0
    list_words = text.split(" ")

    for word in list_words:
        word = word.translate(table)
        if word.isalpha():
            if word.isupper():
                if word != "I":
                    num_capitalized_words += 1

    return num_capitalized_words


def check_capitalization_after_full_stop(text: str):
    num_errors = 0
    list_sent = text.split(".")
    list_sent = [sent for sent in list_sent if sent != '']
    list_sent = [sent.strip() for sent in list_sent]

    for sent in list_sent:
        if sent != "":
            first_letter = sent[0]
            if first_letter.isalpha():
                if not first_letter.isupper():
                    num_errors += 1

    return num_errors

def check_word_of_certain_pattern(text:str):
    pattern=r'2017\S+'
    matches=re.findall(pattern,text)
    return len(matches)




def check_spelling(text: str):
    spell = SpellChecker()
    table = str.maketrans('', '', string.punctuation)
    num_errors = 0
    list_words = text.split(" ")

    for word in list_words:
        if "." not in word:
            word = word.translate(table)
            if word.isalpha():
                word = word.lower()
                if word not in spell:
                    num_errors += 1

    return num_errors

def FeatureExtractor(posted_article:str):
    article={
        "article":[posted_article]
    }
    features=pd.DataFrame(article)

    features["num_single_quote_error"]=features["article"].map(lambda text:check_single_quote_error(text))
    features["num_spacing_error"]=features["article"].map(lambda text:check_spacing_error(text))
    features["num_social_media_handles"]=features["article"].map(lambda text:check_social_media_handle(text))
    features["num_urls_text"]=features["article"].map(lambda text:check_urls(text))
    features["num_twitter_post_urls"]=features["article"].map(lambda text:check_twitter_post_urls(text))
    features["number_of_hastags"]=features["article"].map(lambda text:check_hastags(text))
    features["num_of_absence_of_space_after_sentence_completion"]=features["article"].map(lambda text:check_space_absence_after_sentence_completion(text))
    features["num_capitalized_words"]=features["article"].map(lambda text:check_capatalized_words(text))
    features["num_of_absence_capitalization_after_full_stop"]=features["article"].map(lambda text:check_capitalization_after_full_stop(text))
    features["num_of_words_of_pattern_2017word"]=features["article"].map(lambda text:check_word_of_certain_pattern(text))
    features["num_mispelled_words"]=features["article"].map(lambda text:check_spelling(text))

    features.drop(["article"],axis=1,inplace=True)
    features=np.array(features)
    print("Features extracted....")
    return features
