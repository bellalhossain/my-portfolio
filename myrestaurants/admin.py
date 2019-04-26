# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
import models
from .models import Post
from .models import Job
from .models import Image

admin.site.register(models.Restaurant)
admin.site.register(models.Dish)
admin.site.register(models.RestaurantReview)

admin.site.register(Post)
admin.site.register(Job)
admin.site.register(Image)
