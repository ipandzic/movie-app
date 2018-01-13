import urllib2
from bs4 import BeautifulSoup


my_url = "https://www.rottentomatoes.com/browse/opening/"

page = urllib2.urlopen(my_url)

soup = BeautifulSoup(page, 'html.parser')


x = soup.findAll("script", {"id": "jsonLdSchema"})

print(x)
