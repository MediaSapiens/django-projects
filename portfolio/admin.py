from django.contrib import admin
from portfolio.models import Gallery, Image, VideoFormat
from portfolio.forms import AdminImageWidget, ImageinForm
from django import forms
from django.core.urlresolvers import reverse
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE


class VideoFormatAdmin(admin.ModelAdmin):
    list_display = ('id', 'video_format', 'video_file', 'image', )


class VideoFormatInline(admin.TabularInline):
    model = VideoFormat
    extra = 0


class ImageAdmin(admin.ModelAdmin):

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'image':
            kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(ImageAdmin, self).formfield_for_dbfield(db_field, **kwargs)

    list_display = ('id', 'name', 'gallery', 'context',
                    'is_video', 'image', )

    inlines = [VideoFormatInline]


class ImageInline(admin.StackedInline):#.TabularInline):
    model = Image
    extra = 0
    form = ImageinForm

    class Media:
        js = ('/static/js/collapsed_stacked_inline.js', )


class GalleryAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'description', 'position', )
    list_editable = ('position', )
    inlines = [ImageInline]

    class Media:
        js = (
            '/static/js/jquery-1.7.1.min.js',
            '/static/js/jquery-ui-1.8.18.custom.min.js',
            '/static/js/admin_list_reorder.js',
        )


class TinyMCEFlatPageAdmin(FlatPageAdmin):

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'content':
            return forms.CharField(widget=TinyMCE(
                attrs={'cols': 80, 'rows': 30},
                mce_attrs={'external_link_list_url': reverse('tinymce.views.flatpages_link_list')},
            ))
        return super(TinyMCEFlatPageAdmin, self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(Gallery, GalleryAdmin)
admin.site.register(VideoFormat, VideoFormatAdmin)
admin.site.register(Image, ImageAdmin)

admin.site.unregister(FlatPage)
admin.site.register(FlatPage, TinyMCEFlatPageAdmin)
