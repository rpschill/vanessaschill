# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.contrib import admin
from django.contrib.admin import AdminSite

from adminsortable.admin import SortableAdmin
from django_summernote.admin import SummernoteModelAdmin

from . import models

class DocumentAdmin(SortableAdmin, SummernoteModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    ordering = ['order',]
    list_display = ('title', 'category', 'modified', 'order')
    list_editable = ('category',)
    list_filter = ('category',)
    search_fields = ('title', 'summary')
    readonly_fields = ('created', 'modified')
    
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('title', 'summary', 'image', 'ext_url', 'category', 'slug')
        }),
        )
    

admin.site.register(models.Document, DocumentAdmin)