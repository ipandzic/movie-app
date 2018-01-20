# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views import generic

from .models import Movie


class IndexView(generic.ListView):
    template_name = "core/index.html"
    context_object_name = 'all_movies'

    def get_queryset(self):
        return Movie.objects.all()


class DetailView(generic.DetailView):
    model = Movie
    template_name = "core/detail.html"
