from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.utils import timezone

from .models import Post, Tag
from main.models import Catagory


class PostListView(ListView):

    model = Post
    template_name = 'blog/post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        catagory = Catagory.objects.get(
            name__iexact=self.kwargs['catagory'].replace('-', ' ')
        )
        context.update({
            'now': timezone.now(),
            'catagory': catagory,
            'posts': Post.objects.filter(catagory__name=catagory.name)
        })
        return context


class PostDetailView(DetailView):

    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        context.update({
            'now': timezone.now(),
            'pk': pk,
            'catagory': self.kwargs['catagory'],
            'tags': Post.objects.get(pk=pk).tags.all()
        })
        return context


class TagListView(ListView):

    model = Tag
    template_name = 'blog/tags_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tag = self.kwargs['tag']
        context.update({
            'tag': Tag.objects.get(name__iexact=tag),
            'posts': (
                Post
                .objects
                .filter(tags__name__iexact=tag)
                .order_by('-created_date')
            )
        })
        return context
