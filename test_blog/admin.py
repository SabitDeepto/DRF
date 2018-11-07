from django.contrib import admin

# Register your models here.
from test_blog.models import Post

admin.site.register(Post)
