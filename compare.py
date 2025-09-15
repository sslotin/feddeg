from argparse import ArgumentParser
from tqdm import tqdm
from hashlib import md5


parser = ArgumentParser()
parser.add_argument('file1')
parser.add_argument('file2')

args = parser.parse_args()

def get_hashes(fname: str) -> str:
    """Calculates a set of md5 hashes for every block"""
    hashes = set()
    with open(fname, 'r') as file:
        for line in tqdm(file, desc=f'Reading {fname}', unit=' lines'):
            hashes.add(md5(line.encode('utf-8')).hexdigest())
    return hashes

d1 = get_hashes(args.file1)
d2 = get_hashes(args.file2)

assert d1 <= d2

GREEN = '\033[32m'
RESET = '\033[0m'

print(GREEN, f'{args.file1} is a subset of {args.file2}', RESET)
