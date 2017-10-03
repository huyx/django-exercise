from django.views.generic import ListView

from apps.ex01miniblog.models import Article


class ArticleListView(ListView):
    model = Article

    # 因为是从引用的别的应用中的 model，因此需要明确指定 template_name
    template_name = 'ex04datatables/article_list.html'
