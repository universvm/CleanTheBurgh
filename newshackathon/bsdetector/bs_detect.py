import json

def create_bs_dict():
    """ Creates dictionary with domain name and Value 1 for fake news"""

    # Open BS detector File:
    with open('bs_data.json') as bs_json:
        # Load JSON:
        bs_json = json.load(bs_json)
        # Going through the keys and replace value with 1:
        for key in bs_json.keys():
            bs_json[key] = 1

    # Open TheBlackList (bufala.it) Italian News File:
    with open('bs_italian.txt', 'r+', encoding="utf-8") as bs_italian:
        # Loop through list
        for it_domain in bs_italian.readlines():
            it_domain = it_domain.strip('\n')
            bs_json[it_domain.lower()] = 1

    return bs_json
