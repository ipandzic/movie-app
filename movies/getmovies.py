import json
import os
import re
import urllib2

import bs4
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movies.settings")
django.setup()

from core.models import Movie

url = "https://www.rottentomatoes.com/"
request = urllib2.urlopen(url + "browse/opening/")
soup = bs4.BeautifulSoup(request, 'html.parser')

schema = soup.find("script", {"id": "jsonLdSchema"}).get_text()

movie_list_uni = re.findall(r'\[.+\]', schema)[0][1:-1]
movie_list = movie_list_uni.replace("},{", "};{").split(';')

for item in movie_list:
    item = json.loads(item)
    item_position = item["position"]
    item_movie_url = item["url"]
    item_request = urllib2.urlopen(url + item_movie_url)
    item_soup = bs4.BeautifulSoup(item_request, 'html.parser')
    item_schema = item_soup.findAll("script", {"id": "jsonLdSchema"})[0].get_text()
    item_dict = json.loads(item_schema)
    item_title = item_dict["name"]
    if Movie.objects.filter(title=item_title).exists():
        pass
    else:
        item_production_company = item_dict["productionCompany"]["name"]
        item_img_url = item_soup.find("img", {"class": "posterImage"}).attrs["src"]
        try:
            item_rating = item_dict["aggregateRating"]["ratingValue"]
        except KeyError:
            item_rating = None
        movie_object = Movie(
            position=item_position,
            title=item_title,
            production_company=item_production_company,
            movie_url=item_movie_url,
            image_url=item_img_url,
            rating=item_rating
        )
        movie_object.save()
