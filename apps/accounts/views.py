# apps/accounts/views.py

# Django modules
from django.shortcuts import render
from django.views.generic import ListView

# Locals

# Create your views here.


# CLASS VIEW: Home
class RegisterUser(ListView):
	# model 				= Post 
	template_name 		= 'accounts/register_user.html'
	# context_object_name = 'posts'

	def get_context_data(self, *, object_list=None, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Blog Magazine'
		return context
