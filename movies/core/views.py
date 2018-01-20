# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404

from .models import Movie


def index(request):
    all_movies = Movie.objects.all()
    return render(request, 'core/index.html', {'all_movies': all_movies})


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'core/detail.html', {'movie': movie})
