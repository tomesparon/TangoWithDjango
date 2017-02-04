from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
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