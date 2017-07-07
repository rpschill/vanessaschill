from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Article


def ArticleList(request):
    queryset = Article.objects.filter(published=True).order_by('-published_date')
    paginator = Paginator(queryset, 5) # Show 5 articles per page
    
    page = request.GET.get('page')
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page
        articles = paginator.page(1)
    except EmptyPage:
        # If page is out of range, deliver last page of results
        articles = paginator.page(paginator.num_pages)
    
    return render(request, 'article_list.html', {'articles': articles})


class ArticleDetail(DetailView):
    template_name = 'article_detail.html'
    context_object_name = 'article_detail'
    
    def get_queryset(self):
        articles_filtered = Article.objects.filter(slug=self.kwargs['slug'])
        return articles_filtered
