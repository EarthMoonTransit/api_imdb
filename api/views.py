from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from .models import Category, Genres
from .serializers import *
from .pagination import StandartResultSetPagination

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ('get', 'post', 'delete')
    pagination_class = StandartResultSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]


class GenresViewSet(ModelViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer
    http_method_names = ('get', 'post', 'delete')
    pagination_class = StandartResultSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', ]

class TitleViewSet(ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    pagination_class = StandartResultSetPagination