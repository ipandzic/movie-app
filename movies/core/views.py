# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import Http404
from django.shortcuts import render

from .models import Movie


def index(request):
    all_movies = Movie.objects.all()
    return render(request, 'core/index.html', {'all_movies': all_movies})


def detail(request, movie_id):
    try:
        movie = Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        raise Http404("Movie does not exist.")
    return render(request, 'core/detail.html', {'movie': movie})
