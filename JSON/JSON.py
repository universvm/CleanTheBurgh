import json
import urllib

def load(filename):
    json_string = filename
    parsed_json = json.loads(json_string)
    strs = []
    strs.append(parsed_json['title'])
    strs.append(parsed_json['text'])
    strs.append(parsed_json['source'])
    return strs

#def translate(keyword):

   # query = urllib.urlencode({'q': keyword})
    #response = urllib.urlopen('http://ajax.googleapis.com/ajax/services/search/web?v=1.0&' + query).read()
    #parsed_json2 = json.loads(response)
