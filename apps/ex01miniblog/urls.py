from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ArticleListView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)', views.ArticleDetailView.as_view(), name='detail'),
]
