from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'slug')
        model = Category


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'slug')
        model = Genres


class TitleSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('name', 'year', 'description', 'category', 'genre')
        model = Title