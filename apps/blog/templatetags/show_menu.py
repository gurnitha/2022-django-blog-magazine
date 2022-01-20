# apps/blog/templatetags/menu_tags.py

# Django modules
from django import template

# Locals
from apps.blog.models import Category

# Template library
register = template.Library()

# Register your template here

@register.inclusion_tag('shared/tpl/menu_tpl.html')
def show_menu():
	# categories = Category.objects.all()
	first_three_categories = Category.objects.order_by('id')[0:3]
	# print(first_three_categories) # <-- :)
	
	context = {
		# 'menu_category':categories,
		'first_three_categories':first_three_categories,
	}
	return context