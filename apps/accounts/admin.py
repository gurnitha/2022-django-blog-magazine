# apps/accounts/admin.py

# Django modules
from django.contrib import admin

# Locals
from apps.accounts.models import Author

# Register your models here.


@admin.register(Author)
class CategoryAdmin(admin.ModelAdmin):
	list_display = ('author_name', 'author_slug')
	list_filter = ('created', 'author_name')
	search_fields = ('author_name',)
	prepopulated_fields = {'author_slug': ('author_name',)}