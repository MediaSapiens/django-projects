from django.contrib.admin.widgets import AdminFileWidget
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe
from django import forms


class AdminImageWidget(AdminFileWidget):

    def render(self, name, value, attrs=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name=str(value)
            output.append(u' <a href="%s" target="_blank"><img src="%s" width="102" height="77"alt="%s" /></a> %s ' % \
                (image_url, image_url, file_name, _('Change:')))
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))


class ImageinForm(forms.ModelForm):
    image = forms.ImageField(widget=AdminImageWidget())
    exclude = ('order', )

    class Media:
        js = (
            '/static/js/jquery-1.7.1.min.js',
            '/static/js/jquery-ui-1.8.18.custom.min.js',
            '/static/js/menu-sort.js',
        )
