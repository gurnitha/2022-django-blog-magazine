# apps/accounts/models.py

# Django modules
from django.db import models
from django.contrib.auth.models import User

# Locals

# Create your models here.


# Model:Author
class Author(models.Model):
	author_name = models.OneToOneField(User,on_delete=models.CASCADE,null=True, blank=True)
	author_slug =  models.SlugField(max_length=225, verbose_name='Url', unique=True)
	author_thumbnail = models.ImageField(upload_to='authors/%Y/%m/%d')
	author_short_description = models.CharField(max_length=255, blank=True, null=True)
	author_description = models.TextField(blank=True, null=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ('author_name',)
		verbose_name = 'Author'
		verbose_name_plural = 'Authors'
    	
	def __str__(self):
		return str(self.author_name)