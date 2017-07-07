from __future__ import unicode_literals

from datetime import datetime

from django.db import models
from django.conf import settings
from django.urls import reverse

from model_utils import Choices
from model_utils.fields import StatusField, MonitorField, SplitField
from model_utils.models import TimeStampedModel, StatusModel

from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill


class Authorable(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='articles_authored',
    )
    
    class Meta:
        abstract = True


class Creatable(models.Model):
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='articles_created',
    )
    
    class Meta:
        abstract = True


class Coauthorable(models.Model):
    coauthors = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='articles_coauthored',
        blank=True
    )
    
    class Meta:
        abstract = True


class Featurable(models.Model):
    featured_image = models.ImageField(blank=True, null=True, upload_to='images',)
    featured_image_thumbnail_home = ImageSpecField(
        source='featured_image',
        processors=[ResizeToFill(980, 270)]
        )
    featured_image_thumbnail_blog = ImageSpecField(
        source='featured_image',
        processors=[ResizeToFill(980, 270)]
        )
    featured_image_splash = ImageSpecField(
        source='featured_image',
        processors=[ResizeToFill(1200, 360)]
        )
        
    class Meta:
        abstract = True


class Article(Authorable, Creatable, Coauthorable, Featurable):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    slug = models.SlugField()
    body = SplitField()
    labels = models.ManyToManyField('Label', blank=True,)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('article-detail', args=(self.slug,))


class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField()
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'


class Label(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name
