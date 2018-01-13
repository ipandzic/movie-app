import urllib.request
import bs4


url = "https://www.rottentomatoes.com/browse/opening/"

request = urllib.request.urlopen(url)

soup = bs4.BeautifulSoup(request, 'html.parser')

x = soup.findAll("script", {"id": "jsonLdSchema"})

print(x)
