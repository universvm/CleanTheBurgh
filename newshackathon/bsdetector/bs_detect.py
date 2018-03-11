import json

# parses data and return a list of fake domain.

def create_bs_dict():
    """ Creates dictionary with domain name and Value 1 for fake news"""
    
    bs_list = []
    
    # Open BS detector File:
    with open('bs_data.json') as bs_json:
        # Load JSON:
        bs_json = json.load(bs_json)
        # Going through the keys and replace value with 1:
        for key in bs_json.keys():
            bs_list.append(key)

    # Open TheBlackList (bufala.it) Italian News File:
    with open('bs_italian.txt', 'r+', encoding="utf-8") as bs_italian:
        # Loop through list
        for it_domain in bs_italian.readlines():
            it_domain = it_domain.strip('\n').lower()
            bs_list.append(it_domain)

    return bs_list
