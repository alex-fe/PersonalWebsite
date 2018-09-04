from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import include
from django.urls import path

from blog.views import TagListView
from main.views import splash_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', splash_page,  name='splash'),
    path('<slug:catagory>/', include(('blog.urls', 'blog'), namespace='blog')),
    path('<slug:tag>/', TagListView.as_view(), name='tags'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
