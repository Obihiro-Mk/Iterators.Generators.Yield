import hashlib


def md5_gen(file):
    with open(file, 'r', encoding='utf-8') as f:
        for i in f:
            yield hashlib.md5(i.strip().encode('utf-8')).hexdigest()


for i in md5_gen('country_link.txt'):
    print(i)
