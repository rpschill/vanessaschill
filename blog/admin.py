from datetime import datetime
from django.contrib import admin
from django.contrib.admin import AdminSite

from django_summernote.admin import SummernoteModelAdmin
from imagekit.admin import AdminThumbnail

from . import models

AdminSite.site_title = "Hi-Finn Platform"
AdminSite.site_header = "Hi-Finn Platform Administration"


class ArticleAdmin(SummernoteModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    ordering = ['-published_date', '-last_modified']
    list_display = ('title', 'author', 'category', 'published', 'published_date', 'last_modified', '__str__')
    list_editable = ('published', 'category')
    list_filter = ('published', 'category', 'author')
    search_fields = ('title',)
    readonly_fields = ('last_modified', 'creator', 'published_date')
    view_on_site = True
    admin_thumbnail = AdminThumbnail(image_field='featured_image')
    
    fieldsets = (
        ('Content', {
            'classes': ('wide',),
            'fields': ('title', 'subtitle', 'body', 'author', 'featured_image', 'published'),
        }),
        ('Additional Options', {
            'classes': ('collapse', 'wide'),
            'fields': ('coauthors', 'slug', 'labels', 'category', 'creator', 'published_date', 'last_modified')
        })
        )
    
    def save_model(self, request, obj, form, change):
        if not change:
            # The object is being created so set the user
            obj.creator = request.user
        if obj.published and obj.published_date is None:
            obj.published_date = datetime.now()
        elif not obj.published and obj.published_date is not None:
            obj.published_date = None
        obj.save()


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(models.Article, ArticleAdmin)
admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Label)
