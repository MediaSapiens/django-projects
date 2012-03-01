import uuid
import os
from django.db import models
from django.utils.translation import ugettext_lazy as _

CONTENTTYPES = [u'image', 'video', 'image']


def images(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('images', filename)


class Gallery(models.Model):
    title = models.CharField(_('Gallery title'), max_length=255)
    description = models.TextField(blank=True, null=True)
    position = models.PositiveSmallIntegerField("Position")

    def save(self, *args, **kwargs):
        model = self.__class__

        if self.position is None:
            # Append
            try:
                last = model.objects.order_by('-position')[0]
                self.position = last.position + 1
            except IndexError:
                # First row
                self.position = 0

        return super(Gallery, self).save(*args, **kwargs)

    class Meta:
        ordering = ('position', )

    def __unicode__(self):
        return self.title


class Image(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    gallery = models.ForeignKey(Gallery)
    context = models.TextField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    is_video = models.BooleanField(default=False)

    class Meta:
        ordering = ('order', )

    def __unicode__(self):
        return self.name


class VideoFormat(models.Model):
    video_format = models.CharField(_('Video format'), default='720p',
                              max_length=255, blank=True, null=True)
    video_file = models.FileField(upload_to='videos', blank=True, null=True)
    image = models.ForeignKey(Image)

    def __unicode__(self):
        return 'Video Format #%d' % self.pk
