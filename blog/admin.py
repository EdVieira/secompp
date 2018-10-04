from django.contrib import admin
from .models import Post
# Register your models here.

# No site de admin, registre Post
admin.site.register(Post)