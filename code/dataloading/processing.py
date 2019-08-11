from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


def count_words(text):
    tokens = word_tokenize(text.lower())
    tokens = [_clean(t) for t in tokens]
    lemmatizer = WordNetLemmatizer()
    lemmas = [lemmatizer.lemmatize(t) for t in tokens]
    lemmas = [l for l in lemmas if len(l) > 1]
    return Counter(lemmas)


def _clean(word):
    messy_symbols = r"~!@#$%^&*()_+1234567890-=|}{[]\":;'/.,<>?’`"
    for symbol in messy_symbols:
        word = word.replace(symbol, "")

    return word
