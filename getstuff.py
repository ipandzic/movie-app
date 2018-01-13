import urllib2

my_url = "https://www.rottentomatoes.com/browse/opening/"

page = urllib2.urlopen(my_url)

from bs4 import BeautifulSoup
soup = BeautifulSoup(page, 'html.parser')

import re

x = soup.findAll("script", {"id": "jsonLdSchema"})

print(x)