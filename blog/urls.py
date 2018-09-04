from django.urls import path

from .views import PostDetailView, PostListView, TagListView


urlpatterns = [
    path('', PostListView.as_view(), name='posts'),
    path('<int:pk>/', PostDetailView.as_view(), name='detail'),
    path('<slug:tag>/', TagListView.as_view(), name='tags')
]
