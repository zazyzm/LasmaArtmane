from datetime import datetime
from django.db import models
from django.utils import timezone
from django.utils.timezone import get_current_timezone

from section.models import Section


class Gallery(models.Model):
    """Galleries that belong to a section"""
    name = models.CharField('Name of the gallery',
                            max_length=250,
                            unique=True)
    text = models.TextField('Add a description', blank=True)
    section = models.ForeignKey(Section,
                                on_delete=models.DO_NOTHING,
                                verbose_name='the related section')
    is_active = models.BooleanField('Would you like to show it?', default=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
