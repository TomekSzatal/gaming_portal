from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Game, Article, Review

@login_required
def index(request):
    num_games = Game.objects.count()
    num_articles = Article.objects.count()
    num_reviews = Review.objects.count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_games": num_games,
        "num_articles": num_articles,
        "num_reviews": num_reviews,
        "num_visits": num_visits + 1,
    }

    return render(request, "games/index.html", context=context)


class GameListView(LoginRequiredMixin, generic.ListView):
    model = Game
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        query = (self.request.GET.get("q") or "").strip()

        if query:
            queryset = queryset.filter(title__icontains=query)

        return queryset


class GameDetailView(LoginRequiredMixin, generic.DetailView):
    model = Game


class GameCreateView(LoginRequiredMixin, generic.CreateView):
    model = Game
    fields = "__all__"
    success_url = reverse_lazy("games:game-list")


class GameUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Game
    fields = "__all__"
    success_url = reverse_lazy("games:game-list")


class GameDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Game
    success_url = reverse_lazy("games:game-list")


class ArticleListView(LoginRequiredMixin, generic.ListView):
    model = Article
    paginate_by = 5


class ArticleDetailView(LoginRequiredMixin, generic.DetailView):
    model = Article


class ArticleCreateView(LoginRequiredMixin, generic.CreateView):
    model = Article
    fields = "__all__"
    success_url = reverse_lazy("games:article-list")


class ArticleUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Article
    fields = "__all__"
    success_url = reverse_lazy("games:article-list")


class ArticleDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Article
    success_url = reverse_lazy("games:article-list")


class ReviewListView(LoginRequiredMixin, generic.ListView):
    model = Review
    paginate_by = 5