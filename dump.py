import requests
import json


for node in ['172.25.26.139', '172.25.10.133', '172.25.218.135']:
    height = requests.get(f"http://{node}:6862/blocks/height").json()['height']
    for i in range(1, height, 100):
        for block in requests.get(f"http://{node}:6862/blocks/seq/{i}/{min(i + 99, height)}").json():
            print(json.dumps(block))
