from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from simple_email_confirmation.models import SimpleEmailConfirmationUserMixin


class UserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The Email must be')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username=None, password=None):
        user = self.create_user(
            email,
            password=password,
            is_superuser=True,
        )
        user.is_staff = True
        user.role = 'admin'
        if not username:
            username = email
        user.username = username
        user.save(using=self._db)
        return user


class User(SimpleEmailConfirmationUserMixin, AbstractUser):
    ROLES = (

        ('user', 'user'),
        ('moderator', 'moderator'),
        ('admin', 'admin'),

    )
    first_name = models.TextField(max_length=100, null=True)
    last_name = models.TextField(max_length=100, null=True)
    username = models.CharField(max_length=100, unique=True, null=True)
    bio = models.TextField(null=True)
    email = models.EmailField(max_length=255, unique=True)
    role = models.CharField(
        max_length=50,
        choices=ROLES,
        default=ROLES[0][1]
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(null=True, unique=True)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=255, unique=True)
    year = models.PositiveIntegerField(null=True)
    rating = models.PositiveIntegerField(null=True)
    description = models.TextField(null=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name='titles',
        null=True
    )
    genre = models.ManyToManyField(Genre, related_name='titles')

    def __str__(self):
        return self.name


class Review(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        blank=True, null=True
    )
    text = models.TextField()
    score = models.PositiveIntegerField()
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('title', 'author')


class Comment(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
        null=True
    )
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)


class Rate(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        blank=True, null=True)
    sum_vote = models.PositiveIntegerField(
        default=0
    )
    count_vote = models.PositiveIntegerField(
        default=0
    )

