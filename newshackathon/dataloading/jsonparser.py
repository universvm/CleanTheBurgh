import json

DOMAIN_LABEL = 'source'
TITLE_LABEL = 'title'
BODY_LABEL = 'text'


def load_json_data(filename):
    with open(filename) as file:
        json_data = json.load(file)
        return json_data[DOMAIN_LABEL], json_data[TITLE_LABEL], json_data[BODY_LABEL]
