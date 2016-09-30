from bs4 import BeautifulSoup
from sys import argv
import requests, urllib

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
url = 'http://www.biblegateway.com/passage/?search=%s&version=RVR1960' % (urllib.parse.quote_plus(argv[1]))

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.content, 'html.parser')

container = soup.find('div', {'class': 'result-text-style-normal'})

for child in container:
    try:
        print (child.get_text())
    except:
        pass
