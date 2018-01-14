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
    item = json.loads(item)
    item_position = item["position"]
    item_movie_url = item["url"]
    print(item_movie_url)
    item_request = urllib2.urlopen("https://www.rottentomatoes.com/" + item_movie_url)
    item_soup = bs4.BeautifulSoup(item_request, 'html.parser')
    item_x = item_soup.findAll("script", {"id": "jsonLdSchema"})
    item_text = item_x[0].get_text()
    item_dict = json.loads(item_text)
    item_title = item_dict["name"]
    item_production_company = item_dict["productionCompany"]["name"]
    item_img_url = item_dict["image"]
    try:
        item_rating = item_dict["aggregateRating"]["ratingValue"]
        print(item_rating)
    except KeyError:
        item_rating = 0
        print(item_rating)
    movie_object = Movie(
        position=item_position,
        title=item_title,
        production_company=item_production_company,
        movie_url=item_movie_url,
        image_url=item_img_url,
        rating=item_rating
    )
    movie_object.save()
