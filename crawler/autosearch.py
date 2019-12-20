import sys, requests, bs4, webbrowser

print('请稍候，正在百度中...')
# 设置伪装浏览器的请求 headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36',
    'Host': 'www.baidu.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    }


url = 'https://www.baidu.com/s?wd=' + sys.argv[1:]
res = requests.get(url, headers=headers)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, features="html.parser")

links = []
for i in range(1, 11):
    div = soup.find(id=str(i))
    href = div.find('a').get('href')
    links.append(href)

num_open = min(3, len(links))
for i in range(num_open):
    webbrowser.open(links[i])

