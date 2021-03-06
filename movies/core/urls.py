from django.conf.urls import url

from . import views

app_name = 'core'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^top5/$', views.Top5View.as_view(), name='top5'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^movie/add/$', views.MovieCreate.as_view(), name="movie-add"),
    url(r'^movie/(?P<pk>[0-9]+)/$', views.MovieUpdate.as_view(), name="movie-update"),
    url(r'^movie/(?P<pk>[0-9]+)/delete/$', views.MovieDelete.as_view(), name="movie-delete")
]
