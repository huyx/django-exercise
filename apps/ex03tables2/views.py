from django.views.generic import DetailView
from django_tables2 import SingleTableView

from . import models
from . import tables


class ArticleListView(SingleTableView):
    model = models.Article

    table_class = tables.ArticleTable
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()
    #     table = tables.ArticleTable(self.get_queryset())
    #     RequestConfig(self.request, paginate={'per_page': 2}).configure(table)
    #     context['table'] = table
    #     return context


class ArticleDetailView(DetailView):
    model = models.Article
