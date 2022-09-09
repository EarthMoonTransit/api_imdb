from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from .models import Category, Genres
from .serializers import *
from .pagination import StandartResultSetPagination

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names = ('get', 'post', 'delete')
    pagination_class = StandartResultSetPagination

class GenresViewSet(ModelViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenreSerializer
    http_method_names = ('get', 'post', 'delete')
    pagination_class = StandartResultSetPagination

class TitleViewSet(ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitleSerializer
    pagination_class = StandartResultSetPagination