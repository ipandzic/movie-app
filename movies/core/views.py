# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Movie


class IndexView(generic.ListView):
    template_name = "core/index.html"
    context_object_name = 'all_movies'

    def get_queryset(self):
        return Movie.objects.all()


class DetailView(generic.DetailView):
    model = Movie
    template_name = "core/detail.html"


class MovieCreate(CreateView):
    model = Movie
    fields = ['position', 'title', 'production_company', 'rating', 'movie_url', 'image_url']
