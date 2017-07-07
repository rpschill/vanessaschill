# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import ListView

from .models import Document


class InstructionalList(ListView):
    template_name = 'instructional-design.html'
    queryset = Document.objects.filter(category='instructional').order_by('order')
    context_object_name = 'idocuments'
    

class SalesList(ListView):
    template_name = 'sales.html'
    queryset = Document.objects.filter(category='sales').order_by('order')
    context_object_name = 'sales_objects'
