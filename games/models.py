from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()

    class Meta:
        ordering = ("title",)

    def __str__(self):
        return self.title


class User(AbstractUser):
    bio = models.TextField(blank=True)

    class Meta:
        ordering = ("username",)


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    authors = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="articles")

    class Meta:
        ordering = ("-created_at",)

    def __str__(self):
        return self.title


class Review(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.FloatField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-created_at",)
        unique_together = ("game", "author")

    def __str__(self):
        return f"{self.game} - {self.rating}"