# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Movie(models.Model):
    """
    Describes a movie with properties such as title, year, etc.
    """
    title = models.CharField(max_length=1024)
    content_rating = models.CharField(max_length=1024)
    movie_url = models.CharField(max_length=1024)

    def __str__(self):
        return self.title
