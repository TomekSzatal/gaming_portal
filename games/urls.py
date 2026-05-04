from django.urls import path
from .views import *

app_name = "games"

urlpatterns = [
    path("", index, name="index"),

    path("games/", GameListView.as_view(), name="game-list"),
    path("games/<int:pk>/", GameDetailView.as_view(), name="game-detail"),
    path("games/create/", GameCreateView.as_view(), name="game-create"),
    path("games/<int:pk>/update/", GameUpdateView.as_view(), name="game-update"),
    path("games/<int:pk>/delete/", GameDeleteView.as_view(), name="game-delete"),

    path("articles/", ArticleListView.as_view(), name="article-list"),
    path("articles/<int:pk>/", ArticleDetailView.as_view(), name="article-detail"),
    path("articles/create/", ArticleCreateView.as_view(), name="article-create"),
    path("articles/<int:pk>/update/", ArticleUpdateView.as_view(), name="article-update"),
    path("articles/<int:pk>/delete/", ArticleDeleteView.as_view(), name="article-delete"),

    path("reviews/", ReviewListView.as_view(), name="review-list"),
]