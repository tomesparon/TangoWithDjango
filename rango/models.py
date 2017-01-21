from __future__ import unicode_literals

from django.db import models

# Create your models here.
# . Both must inherit from the Model base class, django.db.models.Model .
class Category(models.Model):
	name = models.CharField(max_length=128, unique=True)
	# Exercise add in attributes as integerfields for views and likes
	views = models.IntegerField(default=0)
	likes = models.IntegerField(default=0)


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