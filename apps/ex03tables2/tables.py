from django_tables2 import tables

from . import models


class ArticleTable(tables.Table):
    class Meta:
        model = models.Article
        fields = ('title', 'created_at', 'actions')
        attrs = {'class': 'plateblue table table-striped'}
