from django.db import models
from django.utils import timezone

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


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    tags = models.ManyToManyField(Tag)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
