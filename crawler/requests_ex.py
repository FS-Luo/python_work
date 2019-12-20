import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
# 检查下载是否成功
res.raise_for_status()

with open('RomeoAndJuliet.txt', 'wb') as f:
    for chunk in res.iter_content(100000):
        f.write(chunk)


