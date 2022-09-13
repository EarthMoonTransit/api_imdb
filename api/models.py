from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.name

class Genres(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.name

class Title(models.Model):
    name = models.CharField(max_length=255, unique=True)
    year = models.PositiveIntegerField(null=True)
    rating = models.PositiveIntegerField(null=True)
    description = models.TextField(null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name='titles', null=True)
    genre = models.ManyToManyField(Genres, related_name='titles')

    def __str__(self):
        return self.name
