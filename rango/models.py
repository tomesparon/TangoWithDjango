from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
# Create your models here.
# . Both must inherit from the Model base class, django.db.models.Model .
# 
# PLEASE ADD A MAX_LEGTH PARAMETER VIA AN ATTRIBUTE TO STORE IT
class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	# Exercise add in attributes as integerfields for views and likes
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)
	#Ch6.3 add slug to clean my urls, and set to blank true
	slug = models.SlugField(blank=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)
	# IF VIEWS LESS 0 then dont

	class Meta:
		verbose_name_plural = 'Categories'

	def __str__(self): # For Python 2, use __unicode__ too
		return self.name

class Page(models.Model):
	category = models.ForeignKey(Category)
	title = models.CharField(max_length=128)
	url = models.URLField()
	views = models.IntegerField(default=0)

	def __str__(self): # For Python 2, use __unicode__ too
		return self.title

class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    # Override the __unicode__() method to return out something meaningful!
    # Remember if you use Python 2.7.x, define __unicode__ too!
    def __str__(self):
        return self.user.username
