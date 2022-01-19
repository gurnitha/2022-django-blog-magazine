# apps/blog/models.py

# Django modules
from django.db import models

# Locals

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=100)