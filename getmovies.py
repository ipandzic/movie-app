import urllib.request
import bs4
import re

url = "https://www.rottentomatoes.com/browse/opening/"

request = urllib.request.urlopen(url)

soup = bs4.BeautifulSoup(request, 'html.parser')

x = soup.findAll("script", {"id": "jsonLdSchema"})

text = x[0].get_text()
match = re.findall(r'\[.+\]', text)[0]


print(match)