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


#### 5. MENU TEMPLATE TAGS Part 3 - Display menu

        Steps:

        1. Fetch menu items in menu_tpl.html using for loop
        2. Load show_menu tamplate tags in header.html
        3. Replace include menu_tpl.html in header.html with show_menu tags {% show_menu %}
        4. Test it out

        NOTE:

        1. After loading the show_menu, you will get errors like this:

            django.template.exceptions.TemplateSyntaxError: ''show_menu'' 
            is not a registered tag library. Must be one of:

            admin_list
            admin_modify
            admin_urls
            cache
            i18n
            l10n
            log
            show_menu
            static

        2. To solve this problem, siply restart your server and refresh your browser

        3. If there are many category menu in the db, the menu bar will look
           so crowded.

        4. NEXT > Limit the display of menu item, and the rest put in dropdown menu

        modified:   README.md
        modified:   templates/shared/header.html
        modified:   templates/shared/tpl/menu_tpl.html


#### 6. MENU TEMPLATE TAGS Part 4 - Limit the menu item by showing last 2 menu item 

        Steps:

        1. Modify show_menu function to show only 3 menu items
        2. Modify menu_tpl by showing about and contact menu

        NOTE:

        1. For now, only 3 menu items showed.
        2. But there are some items do not show

        NEXT> Showing the rest items in dropdown menu

        modified:   README.md
        modified:   apps/blog/templatetags/show_menu.py
        modified:   templates/shared/tpl/menu_tpl.html


#### 7. MENU TEMPLATE TAGS Part 5 - Showing the rest of the menu items in dropdown menu

        Steps:

        1. In show_menu.py load the rest of menu items
        2. In show_menu.py modify first_three_categories to first_two_categories
           and modify the loop in menu_tpl.html accordingly.
        3. In menu_tpl.html fetch and loop the rest of menu item
        4. Test it out :)

        modified:   README.md
        modified:   apps/blog/templatetags/show_menu.py
        modified:   templates/shared/tpl/menu_tpl.html