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
	first_two_categories = Category.objects.order_by('id')[0:2]
	# print(first_three_categories) # <-- :)

	the_rest_categories = Category.objects.order_by('id')[2:10]
	# print(the_rest_categories) # <-- :)

	context = {
		# 'menu_category':categories,
		'first_two_categories':first_two_categories,
		'the_rest_categories':the_rest_categories
	}
	return context


@register.inclusion_tag('shared/tpl/canvas_menu_tpl.html')
def show_canvas_menu():
	first_two_categories_for_canvas_menu = Category.objects.order_by('id')[0:2]
	# print(canvas_menu) # <-- :)

	the_rest_categories_for_canvas_menu = Category.objects.order_by('id')[2:10]
	# print(first_two_categories_for_canvas_menu) # <-- :)

	context = {
		'first_two_categories_for_canvas_menu':first_two_categories_for_canvas_menu,
		'the_rest_categories_for_canvas_menu':the_rest_categories_for_canvas_menu
	}
	return context