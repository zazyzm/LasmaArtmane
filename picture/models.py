from datetime import datetime
from django.db import models
from django.utils.timezone import get_current_timezone

from gallery.models import Gallery


class Picture(models.Model):  # Need to install Pillow
    """Pictures belonging to a gallery"""
    # TYPE_CHOICES = [
    #     ('Picture', 'Picture'),
    #     ('Video', 'Video')
    # ]
    name = models.CharField('Name for the picture',
                            max_length=250,
                            unique=True)
    picture = models.ImageField(upload_to='pictures/%Y/%m/%d/')
    #picture = models.ImageField(upload_to='pictures/%Y/%m/%d/', height_field='height', width_field='width')
    text = models.TextField('Add a description if you wish', blank=True)
    gallery = models.ForeignKey(Gallery,
                                on_delete=models.CASCADE,
                                verbose_name="The related gallery")
    is_active = models.BooleanField(default=True)
    #type = models.CharField(max_length=1, choices=TYPE_CHOICES)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
