from django.db import models
from tinymce import models as tinymce_models
from django.utils.translation import ugettext_lazy as _


class BlogPost(models.Model):
    title = models.CharField(_('BlogPost title'), max_length=255)
    text = tinymce_models.HTMLField()
    sorting = models.PositiveSmallIntegerField("Sorting")
    date = models.DateField()
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ('sorting', )
