from django.conf.urls import url
from . import views


app_name = 'core'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^movie/add/$', views.MovieCreate.as_view(), name="movie-add")
]
