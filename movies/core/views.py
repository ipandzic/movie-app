# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .models import Movie


def index(request):
    all_movies = Movie.objects.all()
    html = ''
    for movie in all_movies:
        url = '/core/' + str(movie.id) + '/'
        html += '<a href="' + url + '">' + movie.title + '</a><br>'
    return HttpResponse(html)


def detail(request, movie_id):
    return HttpResponse("<h2>Details for Movie id: " + str(movie_id) + "</h2>")
