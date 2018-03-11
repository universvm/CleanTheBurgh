import os
import numpy as np
from collections import Counter
from multiprocessing import Pool
from newshackathon.dataloading.jsonparser import load_json_data
from newshackathon.dataloading.processing import count_words
from newshackathon.definitions import REAL_NEWS_DIRECTORY, FAKE_NEWS_DIRECTORY, JSON_SUBDIRECTORY

MAX_WORD_FREQUENCY = 1
MIN_WORD_FREQUENCY = 1 / 8


class DataConstructor(object):
    def __init__(self):
        self._words_counter = Counter()
        real_news = self._load_data(REAL_NEWS_DIRECTORY)
        fake_news = self._load_data(FAKE_NEWS_DIRECTORY)
        self._docs_count = len(real_news) + len(fake_news)
        self._word_index_dict = self._choose_features()
        print('featureset size: {}'.format(len(self._word_index_dict)))
        self._trainset = [self._construct_data_vector(words_frequency, False) for _, _, words_frequency in real_news]
        self._trainset += [self._construct_data_vector(words_frequency, True) for _, _, words_frequency in fake_news]
        self._trainset = np.array(self._trainset)

    def get_trainset(self):
        return self._trainset

    def _load_data(self, directory):
        json_dir = directory + JSON_SUBDIRECTORY
        with Pool(processes=4) as pool:
            data = pool.map(load_json_data, [json_dir + filename for filename in os.listdir(json_dir)])
            data = [d for d in data if d]  # Filter or exceptions

        processed_data = []
        for domain, title, body in data:
            news_words_counter = count_words(body)
            self._words_counter += news_words_counter
            words_count = sum(news_words_counter.values())
            words_frequency = {word: (word_count / words_count) for word, word_count in news_words_counter.items()}
            processed_data.append((domain, title, words_frequency))

        return processed_data

    def _choose_features(self):
        words = [word for word in self._words_counter.keys()
                 if MIN_WORD_FREQUENCY < self._words_counter[word] / self._docs_count < MAX_WORD_FREQUENCY]

        word_index_dict = {}
        for i, word in enumerate(words):
            word_index_dict[word] = i

        return word_index_dict

    def _construct_data_vector(self, words_frequency, is_false):
        data_vector = np.empty(len(self._word_index_dict) + 1)
        data_vector[len(self._word_index_dict)] = int(is_false)
        for word, index in self._word_index_dict.items():
            frequency = words_frequency.get(word, 0)
            data_vector[index] = frequency

        return data_vector
