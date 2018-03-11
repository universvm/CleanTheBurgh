import os
import numpy as np
from collections import Counter
from json.decoder import JSONDecodeError
from urllib3.exceptions import NewConnectionError
from newshackathon.dataloading.jsonparser import load_json_data
from newshackathon.dataloading.processing import count_words
from newshackathon.dataloading.webscraper import scrap_data
from newshackathon.definitions import ROOT_DIR

FAKE_NEWS_DIRECTORY = ROOT_DIR + '../Data/fake/'
REAL_NEWS_DIRECTORY = ROOT_DIR + '../Data/real/'
JSON_SUBDIRECTORY = 'json/'
URLS_FILENAME = 'urls.txt'


def construct_data_set():
    real_news, real_words_counter = _load_data(REAL_NEWS_DIRECTORY)
    fake_news, fake_words_counter = _load_data(FAKE_NEWS_DIRECTORY)
    all_words_counter = real_words_counter + fake_words_counter
    word_index_dict = _choose_features(all_words_counter)

    dataset = [_construct_data_vector(words_frequency, word_index_dict, False) for _, _, words_frequency in real_news]
    dataset += [_construct_data_vector(words_frequency, word_index_dict, True) for _, _, words_frequency in fake_news]
    return np.array(dataset)


def _load_data(directory):
    json_directory = directory + JSON_SUBDIRECTORY
    data = []
    for filename in os.listdir(json_directory):
        try:
            data.append(load_json_data(json_directory + filename))
        except JSONDecodeError:
            print(filename + ' doesn\'t work')

    with open(directory + URLS_FILENAME, "r") as urls_file:
        for url in urls_file:
            try:
                data.append(scrap_data(url))
            except:
                print(url + ' couldn\'t be scraped')

    processed_data = []
    all_words_counter = Counter()
    for domain, title, body in data:
        words_counter = count_words(body)
        all_words_counter += words_counter
        words_count = sum(words_counter.values())
        words_frequency = {word: (word_count / words_count) for word, word_count in words_counter.items()}
        processed_data.append((domain, title, words_frequency))

    return processed_data, all_words_counter


def _choose_features(words_counter):
    words = words_counter.keys()
    word_index_dict = {}
    for i, word in enumerate(words):
        word_index_dict[word] = i

    return word_index_dict


def _construct_data_vector(words_frequency, word_index_dict, is_false):
    data_vector = np.empty(len(word_index_dict) + 1)
    data_vector[len(word_index_dict)] = int(is_false)
    for word, index in word_index_dict.items():
        frequency = words_frequency.get(word, 0)
        data_vector[index] = frequency

    return data_vector