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
	context_object_name = 'posts'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Blog Magazine'
		return context


def PostSingle(request):
	return render(request, 'blog/post_single.html')


def About(request):
	return render(request, 'blog/about.html')


def Contact(request):
	return render(request, 'blog/contact.html')