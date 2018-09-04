import os

from django.db import models


def get_image_path(instance, filename):
    return os.path.join(instance.photo_path, 'splash', filename)


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

    @property
    def photo_path(self):
        return '{}_{}'.format(self.pk, self.name)
