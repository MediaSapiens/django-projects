from django.contrib import admin
from portfolio.models import Gallery, Image, VideoFormat
from portfolio.forms import AdminImageWidget, ImageinForm


class ImageAdmin(admin.ModelAdmin):

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'image':
            kwargs.pop("request", None)
            kwargs['widget'] = AdminImageWidget
            return db_field.formfield(**kwargs)
        return super(ImageAdmin, self).formfield_for_dbfield(db_field, **kwargs)

    list_display = ('id', 'name', 'gallery', 'context',
                    'is_video', 'image', )


class VideoFormatAdmin(admin.ModelAdmin):
    list_display = ('id', 'video_format', 'video_file', 'image', )


class ImageInline(admin.StackedInline):#.TabularInline):
    model = Image
    extra = 0
    form = ImageinForm


class GalleryAdmin(admin.ModelAdmin):

    list_display = ('id', 'title', 'description', 'position', )
    list_editable = ('position', )
    inlines = [
        ImageInline,
    ]

    class Media:
        js = (
            '/static/js/jquery-1.7.1.min.js',
            '/static/js/jquery-ui-1.8.18.custom.min.js',
            '/static/js/admin_list_reorder.js',
        )


admin.site.register(Gallery, GalleryAdmin)
admin.site.register(VideoFormat, VideoFormatAdmin)
admin.site.register(Image, ImageAdmin)
