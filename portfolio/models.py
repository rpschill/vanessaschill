# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.urls import reverse

from adminsortable.models import SortableMixin

from model_utils import Choices
from model_utils.models import TimeStampedModel

from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill


class Document(TimeStampedModel, SortableMixin):
    CATEGORY = Choices(
        ('instructional', ('Instructional Design')),
        ('sales', ('Sales'))
        )
    category = models.CharField(choices=CATEGORY, default='instructional', max_length=30)
    title = models.CharField(max_length=250)
    slug = models.SlugField()
    summary = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='images')
    featured_image = ImageSpecField(
        source='image',
        processors=[ResizeToFill(540, 255)]
        )
    ext_url = models.URLField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['order']
        
    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)
