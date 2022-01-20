# apps/blog/admin.py

# Django modules
from django.contrib import admin

# Locals
from apps.blog.models import Category, Tag, Post

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('category_name', 'category_slug')
	list_filter = ('created', 'category_name')
	search_fields = ('category_name',)
	prepopulated_fields = {'category_slug': ('category_name',)}


@admin.register(Tag)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('tag_name', 'tag_slug')
	list_filter = ('created', 'tag_name')
	search_fields = ('tag_name',)
	prepopulated_fields = {'tag_slug': ('tag_name',)}


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('post_title', 'post_slug', 'author_id', 'post_publish', 'post_status')
	list_filter = ('post_status', 'created', 'post_publish', 'author_id')
	search_fields = ('post_title', 'post_description')
	prepopulated_fields = {'post_slug': ('post_title',)}
	raw_id_fields = ('author_id',)
	date_hierarchy = 'post_publish'
	ordering = ('post_status', 'post_publish')