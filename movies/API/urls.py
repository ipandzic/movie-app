from django.conf.urls import url

from .views import MovieDetailAPIView, MovieListAPIView

app_name = 'API'

urlpatterns = [
    url(r'^$', MovieListAPIView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', MovieDetailAPIView.as_view(), name='detail')
]
