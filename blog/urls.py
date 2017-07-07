from django.conf.urls import url, include
from blog import views
from .models import Article


urlpatterns = [
    url(r'^$', views.ArticleList, name='article-list'),
    url(r'^(?P<slug>[\w-]+)/$', views.ArticleDetail.as_view(), name='article-detail'),
]
