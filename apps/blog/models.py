# apps/blog/models.py

# Django modules
from django.db import models
from django.utils import timezone

# Locals
from apps.accounts.models import Author 

# Create your models here.


# Model:Category
class Category(models.Model):
	category_name = models.CharField(max_length=100)
	category_slug = models.SlugField(max_length=225, verbose_name='Url', unique=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True) 

	class Meta:
		ordering = ('category_name',)
		verbose_name = 'Category'
		verbose_name_plural = 'Categories'
    	
	def __str__(self):
		return self.category_name


# Model:Tag
class Tag(models.Model):
	tag_name = models.CharField(max_length=50)
	tag_slug =  models.SlugField(max_length=225, verbose_name='Url', unique=True)
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True) 

	class Meta:
		ordering = ('tag_name',)
		verbose_name = 'Tag'
		verbose_name_plural = 'Tag'
    	
	def __str__(self):
		return self.tag_name



# Model:Post
class Post(models.Model):

    STATUS_POST_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    POST_TYPE_CHOICES = (
        ('featured', 'featured'),
        ('latest', 'latest'),
        ('recent', 'recent'),
        ('popular', 'popular'),
        ('editor_pick', 'editor_pick'),
        ('trending', 'trending'),
    )	

    post_title = models.CharField(max_length=255)
    post_slug    = models.SlugField(max_length=255, verbose_name='Url', unique=True)
    category_id = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    tag_id    = models.ManyToManyField(Tag, blank=True, related_name='posts')
    author_id = models.ForeignKey(Author, on_delete=models.PROTECT, related_name='posts')
    post_content = models.TextField(blank=True)
    post_publish = models.DateTimeField(default=timezone.now)
    post_thumbnail   = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=False)
    post_views   = models.IntegerField(default=0, verbose_name='Times of viewed')
    post_status = models.CharField(choices=STATUS_POST_CHOICES, max_length=15, default='draft')
    post_type = models.CharField(choices=POST_TYPE_CHOICES,max_length=20, default='latest')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.post_title
        
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ('-post_publish',)