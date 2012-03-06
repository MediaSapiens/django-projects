from django.contrib import admin
from blog.models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'date', 'active', 'sorting', )

admin.site.register(BlogPost, BlogPostAdmin)
