# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Movie


class MovieAdmin(admin.ModelAdmin):
    list_display = ["title", "production_company", "rating"]
    list_filter = ["production_company"]
    search_fields = ["title", "production_company"]

    class Meta:
        model = Movie


admin.site.register(Movie, MovieAdmin)
