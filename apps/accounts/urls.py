# apps/accounts/urls.py

# Django modules
from django.urls import path 

# Locals
from apps.accounts.views import *

app_name = 'accounts'


urlpatterns = [
	path('accounts/', RegisterUser.as_view(), name='register')
]