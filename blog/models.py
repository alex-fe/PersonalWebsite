import os
import markdown

from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.html import mark_safe

from main.models import Catagory


class Tag(models.Model):
    """
    name: Name of the tag
    detail: Notes about the tag (optional)
    creation_date: Date when 1st instance of tag was created
    """
    name = models.CharField(max_length=50)
    detail = models.TextField(blank=True)
    creation_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


def get_image_path(instance, filename):
    return os.path.join(instance.name, 'posts', filename)


def markdown_to_html(markdown_text, images):
    image_reference = '\n'.join(
        '[{0.name}]: {0.image.url}'.format(image) for image in images
    )
    md = '{}\n{}'.format(markdown_text, image_reference)
    html = markdown.markdown(md)
    return html


class Image(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to=get_image_path)

    def __str__(self):
        return self.name

    @property
    def get_absolute_url(self):
        return settings.MEDIA_URL + self.image.url


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    images = models.ManyToManyField(Image, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    tags = models.ManyToManyField(Tag)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ('-created_date', )

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def body_html(self):
        return mark_safe(markdown_to_html(self.text, self.images.all()))
