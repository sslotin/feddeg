import json
import hashlib


with open('testedg.deg.rt.ru.har', 'r') as file:
    data = json.loads(file.read())
    for entry in data['log']['entries']:
        if entry['_resourceType'] in ['document', 'script'] and 'text' in entry['response']['content']:
            print(hashlib.md5(entry['response']['content']['text'].encode('utf-8')).hexdigest(), entry['request']['url'])