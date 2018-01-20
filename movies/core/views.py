# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

from .models import Movie


def index(request):
    all_movies = Movie.objects.all()
    template = loader.get_template('core/index.html')
    context = {
        'all_movies': all_movies,
    }
    return HttpResponse(template.render(context, request))


def detail(request, movie_id):
    return HttpResponse("<h2>Details for Movie id: " + str(movie_id) + "</h2>")
