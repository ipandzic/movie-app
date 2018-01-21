# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models


class Movie(models.Model):
    """
    Describes a movie with properties such as title, production_company, etc.
    """
    position = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=1024, blank=True, null=True)
    production_company = models.CharField(max_length=1024, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    movie_url = models.CharField(max_length=1024, blank=True, null=True)
    image_url = models.CharField(max_length=1024, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('core:detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.title
