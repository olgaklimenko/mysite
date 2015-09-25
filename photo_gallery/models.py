from django.db import models
from photo_gallery.fields import ThumbnailImageField
import datetime
from django.utils import timezone
from django.core.urlresolvers import reverse

class Item(models.Model):
    name = models.CharField(max_length = 250)
    description = models.TextField()

    class Meta:
        ordering = ['name']

    def __unicode__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('item_detail', args=[str(self.id)])

class Photo(models.Model):
    item = models.ForeignKey(Item)
    title = models.CharField(max_length = 100)
    image = ThumbnailImageField(upload_to='photos')
    caption = models.CharField(max_length = 250, blank = True)
    votes = models.IntegerField(default = 0)
    class Meta:
        ordering = ['title']

    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('photo_detail',  args=[str(self.id)])

