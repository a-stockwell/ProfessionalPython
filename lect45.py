from bs4 import BeautifulSoup
import urllib.request

#req = urllib.request.urlopen('http://www.nationaljournal.com/politics?rss=1')
req = urllib.request.urlopen('http://feeds.bbci.co.uk/news/rss.xml')
xml = BeautifulSoup(req, 'xml')

for title in xml.findAll('link')[2:]:
    url = title.text
    news = urllib.request.urlopen(url).read
    print(news)
    print(35*"=")
