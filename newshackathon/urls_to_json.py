from multiprocessing import Pool
from newshackathon.dataloading.jsonparser import save_json_data
from newshackathon.dataloading.webscraper import scrap_data
from newshackathon.definitions import FAKE_NEWS_DIRECTORY, REAL_NEWS_DIRECTORY, JSON_SUBDIRECTORY, URLS_FILENAME

pool = Pool(processes=4)
with open(REAL_NEWS_DIRECTORY + URLS_FILENAME) as real_urls:
    real_news = pool.map(scrap_data, real_urls)
    real_news = [news for news in real_news if news]
for i in range(len(real_news)):
    save_json_data(*real_news[i], '{}real{}.json'.format(REAL_NEWS_DIRECTORY + JSON_SUBDIRECTORY, i))


with open(FAKE_NEWS_DIRECTORY + URLS_FILENAME) as fake_urls:
    fake_news = pool.map(scrap_data, fake_urls)
    fake_news = [news for news in fake_news if news]
for i in range(len(fake_news)):
    save_json_data(*fake_news[i], '{}fake{}.json'.format(FAKE_NEWS_DIRECTORY + JSON_SUBDIRECTORY, i))
