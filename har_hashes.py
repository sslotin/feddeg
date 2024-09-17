import json
import hashlib

import argparse


parser = argparse.ArgumentParser()

parser.add_argument('file', type=str)
args = parser.parse_args()

with open(args.file, 'r') as file:
    data = json.loads(file.read())
    for entry in data['log']['entries']:
        if entry['_resourceType'] in ['document', 'script'] and 'text' in entry['response']['content']:
            print(hashlib.md5(entry['response']['content']['text'].encode('utf-8')).hexdigest(), entry['request']['url'])
