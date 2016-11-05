from __future__ import unicode_literals
from django.db import models
from django.db.models.signals import pre_save
from django import forms
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.conf import settings
# Create your models here.



class Post(models.Model):
	title = models.CharField(max_length=200)
	subtitle = models.CharField(max_length=200)
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
	image = models.FileField(null=True, blank=True)
	content = RichTextField()
	category = models.CharField(max_length=200)
	draft = models.BooleanField(default=False)
	slug = models.SlugField(unique=True)
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title

	class Meta:
		ordering = ["-timestamp","-updated"]

class Contact(models.Model):
	name = models.CharField(max_length=200)
	email = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	phone = models.CharField(max_length=200)
	message = models.TextField()
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	
	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name
