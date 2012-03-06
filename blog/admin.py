from django.contrib import admin
from blog.models import BlogPost


class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'date', 'active', 'sorting', )
    list_editable = ('sorting', )

    class Media:
        js = (
            '/static/js/jquery-1.7.1.min.js',
            '/static/js/jquery-ui-1.8.18.custom.min.js',
            '/static/js/blog/admin_list_reorder.js',
        )


admin.site.register(BlogPost, BlogPostAdmin)
