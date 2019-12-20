import os, requests, bs4

url = 'https://xkcd.com'
os.makedirs('xkcd', exist_ok=True)

i = 0

while not url.endswith('#'):
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')

    links = soup.select('#comic img')
    if links != []: 
        comic_url = 'https:' + links[0].get('src')
        
        res = requests.get(comic_url)
        res.raise_for_status()

        with open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb') as image:
            for chunk in res.iter_content():
                image.write(chunk)
        print('Downloading image from ' + comic_url + ' ...')
    # prev button
    prev_link = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prev_link.get('href')
    
    i += 1
    if i == 5:
        print('Completed all tasks!')
        break

