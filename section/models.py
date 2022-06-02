
from django.db import models


class Section(models.Model):
    """Section that consists of galleries"""
    name = models.CharField('name of the section',
                            max_length=250,
                            unique=True)
    text = models.TextField('add a description if you wish', blank=True)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
