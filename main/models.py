import os

from django.db import models
from django.utils.html import escape
from django.utils.text import slugify


def get_image_path(instance, filename):
    filename = '{}{}'.format(
        escape(slugify(instance.name.lower())), os.path.splitext(filename)[1]
    )
    return filename


class Catagory(models.Model):
    """
    name: Name of the Catagory
    detail: Description of the Catagory
    image: Cover photo
    """
    name = models.CharField(max_length=50)
    detail = models.TextField(blank=True)
    image = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    def __str__(self):
        return self.name
