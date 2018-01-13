import os
import django
import urllib2
import bs4
import re
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movies.settings")
django.setup()

from core.models import Movie

url = "https://www.rottentomatoes.com/browse/opening/"

request = urllib2.urlopen(url)

soup = bs4.BeautifulSoup(request, 'html.parser')

x = soup.findAll("script", {"id": "jsonLdSchema"})

text = x[0].get_text()

match = re.findall(r'\[.+\]', text)[0][1:-1]
match = match.replace("},{", "};{")


match_list = match.split(';')


for item in match_list:
    print(json.loads(item)["url"])
    movie_object = Movie(
        movie_url=json.loads(item)["url"]
    )
    movie_object.save()
