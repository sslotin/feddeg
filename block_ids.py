import requests
import json
import time

requests.packages.urllib3.disable_warnings() 

url = 'https://stat.vybory.gov.ru/api/blocks/search'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

blocks = {}

while True:
    new_blocks = json.loads(requests.post(url, json=json.loads('{"shard": null, "height": null}'), headers=headers, verify=False).text)['data']['results']
    for block in new_blocks:
        blocks[block['id']] = block
    print(new_blocks[0])
    time.sleep(60)
