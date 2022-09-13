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
    #category = serializers.SlugRelatedField(slug_field='slug',
    #                                        queryset=Category.objects.all()
    #        )
    #genre = serializers.SlugRelatedField(many=True,
    #                                     slug_field='slug',
    #                                     queryset=Genres.objects.all()
    #                                    )
    category = CategorySerializer(read_only=True)
    genre = GenreSerializer(many=True, read_only=True)

    class Meta:
        fields = ('id', 'name', 'year', 'rating', 'description', 'genre', 'category')
        model = Title