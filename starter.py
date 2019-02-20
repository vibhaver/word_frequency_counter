import requests
from bs4 import BeautifulSoup
import operator


def start(url):
    word_list = []
    source_code = requests.get(url).text                                # accessing web page, and taking only text data
    # print(source_code)
    soup = BeautifulSoup(source_code, features="html.parser")
    # print(soup.get_text())
    # print(soup)

    for post_text in soup.find_all('p'):            # which specific data you want
        print(post_text)
        words = str(post_text)
        content = words.split(" ")
        for each_word in content:
            # print(each_word)
            word_list.append(each_word)
    clean_list(word_list)


def clean_list(word_list):       # removing special symbols
    clean_up_list = []
    for word in word_list:
        symbols = "!@#$%^&*()_+{}|:?~\"|/<>[]`.,=-"
        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], " ")
            # final_split = word.split(" ")
        if len(word) > 0:               # word should exist
            print(word)
            clean_up_list.append(word)
    dictionary(clean_up_list)


def dictionary(clean_up_list):
    word_count = {}
    for word in clean_up_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    for key, value in sorted(word_count.items(), key=operator.itemgetter(1)):
        print(key, value)


start('https://en.wikipedia.org/wiki/Cloud_computing')
