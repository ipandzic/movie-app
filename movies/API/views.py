from rest_framework.generics import ListAPIView, RetrieveAPIView

from core.models import Movie

from .serializers import MovieSerializer


class MovieListAPIView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class MovieDetailAPIView(RetrieveAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
