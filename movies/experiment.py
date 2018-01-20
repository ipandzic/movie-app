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

x = soup.find("script", {"id": "jsonLdSchema"})
print(x)
print(type(x))
text = x.get_text()
print(text)
print(type(text))
movie_links = re.findall(r'\[.+\]', text)[0][1:-1]


#movie_links = movie_links.replace("},{", "};{")


#movie_links = movie_links.split(';')


'''
for item in match_list:
    item = json.loads(item)
    item_position = item["position"]
    item_movie_url = item["url"]
    print(item_movie_url)
    item_request = urllib2.urlopen("https://www.rottentomatoes.com/" + item_movie_url)
    item_soup = bs4.BeautifulSoup(item_request, 'html.parser')
    item_x = item_soup.find("script", {"id": "jsonLdSchema"})
    print(type(item_x))
    print(item_x)
'''
    #item_text = item_x[0].get_text()


    #item_dict = json.loads(item_text)
    #item_title = item_dict["name"]
    #item_production_company = item_dict["productionCompany"]["name"]
