# 2022-django-blog-magazine
Building A Blog Magazine using Django version 3.2.7
https://github.com/gurnitha/2022-django-blog-magazine



#### 1. Basics static setup with postgres database

        .
        ├── LICENSE
        ├── README.md
        ├── apps
        │   ├── accounts
        │   └── blog
        ├── config
        │   ├── __init__.py
        │   ├── __pycache__
        │   ├── asgi.py
        │   ├── settings.py
        │   ├── static
        │   ├── urls.py
        │   └── wsgi.py
        ├── db.sqlite3
        ├── manage.py
        ├── requirements.txt
        └── templates
            ├── base.html
            ├── haed.html
            └── shared

        modified:   .gitignore
        modified:   README.md

        NOTE: Static files are ignored by git


#### 2. Create Category, Tag, Post and Author models

        modified:   README.md
        modified:   apps/accounts/admin.py
        modified:   apps/accounts/models.py
        modified:   apps/blog/admin.py
        modified:   apps/blog/models.py


#### 3. MENU TEMPLATE TAGS Part 1 - Create menu template and include

        Steps:

        1. Create a new folder  : templates/shared/tpl
        2. Create a new file    : templates/shared/tpl/menu_tpl.html
        3. Move menu list from share/header.html to menu_tpl.html
        4. Include menu_tpl.html in header.html


        modified:   README.md
        modified:   templates/shared/header.html
        new file:   templates/shared/tpl/menu_tpl.html


#### 4. MENU TEMPLATE TAGS Part 2 - Create show_menu function

        Steps:

        1. Create folder                : apps/blog/templatetags
        2. Create init files            : apps/blog/templatetags/__init__.py
        3. Create show_menu template    : apps/blog/templatetags/show_menu.py
        4. Define show_menu function    : apps/blog/templatetags/show_menu.py

        modified:   README.md
        new file:   apps/blog/templatetags/__init__.py
        new file:   apps/blog/templatetags/show_menu.py