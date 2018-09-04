from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.utils import timezone

from .models import Post, Tag


class PostListView(ListView):

    model = Post
    template_name = 'blog/post_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['catagory'] = self.kwargs['catagory'].upper()
        context['posts'] = Post.objects.filter(
            catagory__name__iexact=self.kwargs['catagory']
        ).order_by('-created_date')
        return context


class PostDetailView(DetailView):

    model = Post
    template_name = 'blog/post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs['pk']
        post = Post.objects.get(pk=pk)
        context.update({
            'now': timezone.now(),
            'pk': pk,
            'category': self.kwargs['catagory'],
            'tags': post.tags.order_by('-creation_date')
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
