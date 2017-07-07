# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from blog.models import Article


class HomePage(ListView):
    template_name = 'index.html'
    queryset = Article.objects.filter(published=True).order_by('-published_date')[:4]
    

class InstructionalDesign(TemplateView):
    template_name = 'instructional-design.html'


class Sales(TemplateView):
    template_name = 'sales.html'
