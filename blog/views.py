from django.shortcuts import render
from django.views.generic.list import ListView
from django.utils import timezone

from .models import Post, Tag

class PostListView(ListView):

    model = Post
    template_name = 'personal_site/templates/blog/post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context
