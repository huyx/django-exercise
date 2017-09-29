from django.views.generic import ListView, DetailView

from . import models


class ArticleListView(ListView):
    model = models.Article


class ArticleDetailView(DetailView):
    model = models.Article
