# apps/blog/urls.py

# Django modules
from django.urls import path 

# Locals
from apps.blog.views import *

app_name = 'blog'


urlpatterns = [
	path('', PostList.as_view(), name='post_list'),
	path('post/1', PostSingle, name='post_single'),
	path('about/', About, name='about'),
	path('contact/', Contact, name='contact'),
]