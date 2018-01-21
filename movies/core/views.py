# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
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


class MovieUpdate(UpdateView):
    model = Movie
    fields = ['position', 'title', 'production_company', 'rating', 'movie_url', 'image_url']


class MovieDelete(DeleteView):
    model = Movie
    success_url = reverse_lazy('core:index')
