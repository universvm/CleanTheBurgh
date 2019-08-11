import json

DOMAIN_LABEL = 'source'
TITLE_LABEL = 'title'
BODY_LABEL = 'text'


def load_json_data(filename):
    try:
        with open(filename) as file:
            json_data = json.load(file)
            return json_data[DOMAIN_LABEL], json_data[TITLE_LABEL], json_data[BODY_LABEL]
    except:
        print('Couldn\'t parse {} file'.format(filename))


def save_json_data(domain, title, body, filename):
    json_data = {
        DOMAIN_LABEL: domain,
        TITLE_LABEL: title,
        BODY_LABEL: body
    }

    with open(filename, 'w') as file:
        file.write(json.dumps(json_data))