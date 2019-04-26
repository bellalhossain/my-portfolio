# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from datetime import date
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

from sorl.thumbnail import get_thumbnail

#from .managers import JobManager, ImageManager
#from .conf import settings

class Restaurant(models.Model):
    name = models.TextField()
    street = models.TextField(blank=True, null=True)
    number = models.IntegerField(blank=True, null=True)
    city = models.TextField(default="")
    zipCode = models.TextField(blank=True, null=True)
    stateOrProvince = models.TextField(blank=True, null=True)
    country = models.TextField(blank=True, null=True)
    telephone = models.TextField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)
	

    def __unicode__(self):
        return u"%s" % self.name
    def get_absolute_url(self):
        return reverse('myrestaurants:restaurant_detail', kwargs={'pk': self.pk})

class Dish(models.Model):
    name = models.TextField()
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField('Euro amount', max_digits=8, decimal_places=2, blank=True,
        null=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)
    image = models.ImageField(upload_to="myrestaurants", blank=True, null=True)
    restaurant = models.ForeignKey(Restaurant, null=True, related_name='dishes')

    def __unicode__(self):
        return u"%s" % self.name
    def get_absolute_url(self):
        return reverse('myrestaurants:dish_detail', kwargs={'pkr': self.restaurant.pk, 'pk': self.pk})

class Review(models.Model):
    RATING_CHOICES = ((1, 'one'), (2, 'two'), (3, 'three'), (4, 'four'), (5, 'five'))
    rating = models.PositiveSmallIntegerField('Rating (stars)', blank=False, default=3, choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, default=1)
    date = models.DateField(default=date.today)

    class Meta:
        abstract = True

class RestaurantReview(Review):
    restaurant = models.ForeignKey(Restaurant)

class Job(models.Model):
    name = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    updated = models.DateTimeField(auto_now=True)

    #objects = JobManager()

    def __unicode__(self):
        return u"%s" % self.name

    def clean(self):
        self.name = self.name
        self.description = self.description

    def image(self):
        return self.images.visible().order_by('order').first()

    def get_absolute_url(self):
        return reverse('myrestaurants:dish_detail', kwargs={'pkr': self.restaurant.pk, 'pk': self.pk})
	#-------------------Image---------------------
	

class Image(models.Model):
    job = models.ForeignKey(Job, related_name='images')
    image = models.ImageField(upload_to="myrestaurants", blank=True, null=True)
    order = models.PositiveIntegerField()
    width = models.PositiveIntegerField(default=0, blank=True)
    height = models.PositiveIntegerField(default=0, blank=True)
    active = models.BooleanField(default=True)
    uploaded = models.DateTimeField(auto_now_add=True)

    #objects = ImageManager()

    def __unicode__(self):
        return u"%s (%s)" % (self.image, self.job.name)

    @property
    def small_url(self):
        im = get_thumbnail(self.image, settings.IMAGE_SMALL_SIZE, crop="center")
        return im.url

    @property
    def arrow_url(self):
        im = get_thumbnail(self.image, settings.IMAGE_ARROW, crop="center")
        return im.url

    @property
    def medium_url(self):
        im = get_thumbnail(self.image, settings.IMAGE_MEDIUM_SIZE)
        return im.url

    @property
    def large_url(self):
        im = get_thumbnail(self.image, settings.IMAGE_LARGE_SIZE)
        return im.url

    @property
    def extra_large_url(self):
        im = get_thumbnail(self.image, settings.IMAGE_EXTRA_LARGE_SIZE)
        return im.url

    @property
    def original_url(self):
        return self.image.url
#------------------image---------------------------------------------------
	
class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
	
    def __str__(self):
        return self.title