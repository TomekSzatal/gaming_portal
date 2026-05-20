from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User, Game, Article, Review


class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ("bio",)


class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = "__all__"


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = "__all__"


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ("game", "rating", "comment")