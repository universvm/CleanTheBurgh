import os
import numpy as np
from collections import Counter
from multiprocessing import Pool
from newshackathon.dataloading.jsonparser import load_json_data
from newshackathon.dataloading.processing import count_words
from newshackathon.definitions import REAL_NEWS_DIRECTORY, FAKE_NEWS_DIRECTORY, JSON_SUBDIRECTORY

MAX_WORD_FREQUENCY = 1
MIN_WORD_FREQUENCY = 1 / 8


def construct_data_set():
    real_news, real_words_counter = _load_data(REAL_NEWS_DIRECTORY)
    fake_news, fake_words_counter = _load_data(FAKE_NEWS_DIRECTORY)
    all_words_counter = real_words_counter + fake_words_counter

    word_index_dict = _choose_features(all_words_counter, len(fake_news) + len(real_news))
    print('featureset size: {}'.format(len(word_index_dict)))

    dataset = [_construct_data_vector(words_frequency, word_index_dict, False) for _, _, words_frequency in real_news]
    dataset += [_construct_data_vector(words_frequency, word_index_dict, True) for _, _, words_frequency in fake_news]
    return np.array(dataset)


def _load_data(directory):
    json_dir = directory + JSON_SUBDIRECTORY
    with Pool(processes=4) as pool:
        data = pool.map(load_json_data, [json_dir + filename for filename in os.listdir(json_dir)])
        data = [d for d in data if d]  # Filter or exceptions

    processed_data = []
    all_words_counter = Counter()
    for domain, title, body in data:
        words_counter = count_words(body)
        all_words_counter += words_counter
        words_count = sum(words_counter.values())
        words_frequency = {word: (word_count / words_count) for word, word_count in words_counter.items()}
        processed_data.append((domain, title, words_frequency))

    return processed_data, all_words_counter


def _choose_features(words_counter, documents_count):
    words = [word for word in words_counter.keys()
             if MIN_WORD_FREQUENCY < words_counter[word] / documents_count < MAX_WORD_FREQUENCY]

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