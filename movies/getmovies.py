import os
import django
import urllib2
import bs4
import re
import json
import ast
from ast import literal_eval
from collections import MutableMapping

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

counter = 0


for item in match_list:
    item = json.loads(item)
    item_url = item["url"]
    item_position = item["position"]
    print(item_url)
    item_request = urllib2.urlopen("https://www.rottentomatoes.com/" + item_url)
    item_soup = bs4.BeautifulSoup(item_request, 'html.parser')
    item_x = item_soup.findAll("script", {"id": "jsonLdSchema"})
    item_text = item_x[0].get_text()
    print(type(item_text))
    item_name = json.loads(item_text)["name"]
    movie_object = Movie(
        movie_url=item_url,
        position=item_position,
        title=item_name
    )
    movie_object.save()
