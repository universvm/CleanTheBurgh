import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from newshackathon.textprocessing.processing import count_words


def scrap_data(url):
    source = requests.get(url, timeout=20)
    if not source:
        raise ConnectionError('Couldn\'t get a source from {}'.format(source))

    soup = BeautifulSoup(source.text, 'html.parser')
    article_container = _extract_article_container(soup)
    if not article_container:
        raise ConnectionError('Couldn\'t find any article at {}'.format(source))

    domain = _extract_domain(url)
    title = _extract_title(article_container)
    body = _extract_body(article_container)
    return domain, title, body


def _extract_domain(url):
    parsed = urlparse(url)
    domain = '{uri.netloc}'.format(uri=parsed)
    return domain


def _extract_article_container(soup):
    if soup.find('div', {'class': 'post'}):
        return soup.find('div', {'class': 'post'})

    if soup.find('div', {'class': 'article-container'}):
        return soup.find('div', {'class': 'article-container'})

    if soup.find('div', {'class': 'article-text'}):
        return soup.find('div', {'class': 'article-text'})

    if soup.find('article', {'class': 'a-main'}):
        return soup.find('article', {'class': 'a-main'})

    if soup.find('div', {'class': 'js-article-inner'}):
        return soup.find('div', {'class': 'js-article-inner'})

    if soup.article:
        return soup.article

    if soup.find('div', {'class': 'story-body'}):
        return soup.find('div', {'class': 'story-body'})

    if soup.find('div', {'id': 'content-start'}):
        return soup.find('div', {'id': 'content-start'})

    if soup.find('div', {'class': 'entry-content'}):
        return soup.find('div', {'class': 'entry-content'})

    if soup.find('div', {'class': 'td-post-content'}):
        return soup.find('div', {'class': 'td-post-content'})

    if soup.find('div', {'class': 'theiaPostSlider_slides'}):
        return soup.find('div', {'class': 'theiaPostSlider_slides'})

    return None


def _extract_title(article):
    if article.h1:
        return article.h1.getText().strip()

    if article.h2:
        return article.h2.getText().strip()

    if article.header:
        return article.header.getText().strip()

    return None


def _extract_body(article):
    return ' '.join([p.getText().strip() for p in(article.findAll('p') + article.findAll('span'))])