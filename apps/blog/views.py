# apps/blog/views.py

# Django modules
from django.shortcuts import render
from django.views.generic import ListView

# Locals
from apps.blog.models import Post  

# Create your views here.


# CLASS VIEW: Home
class PostList(ListView):
	model 				= Post 
	template_name 		= 'blog/post_list.html'
	context_object_name = 'post_list'

	def get_context_data(self, **kwargs):
		# To get contex, first, call base implementation
		context = super().get_context_data(**kwargs)
		# Load post by featured and the category it belongs to
		context['post_featured'] = Post.objects.filter(post_type='featured')
		# Load post by popular
		context['post_popular'] = Post.objects.filter(post_type='popular')
		context['title'] = 'Blog Magazine'
		return context

	# def get_context_data(self, *, object_list=None, **kwargs):
	# 	context = super().get_context_data(**kwargs)
	# 	context['title'] = 'Blog Magazine'
	# 	return context


def PostSingle(request):
	return render(request, 'blog/post_single.html')


def About(request):
	return render(request, 'blog/about.html')


def Contact(request):
	return render(request, 'blog/contact.html')