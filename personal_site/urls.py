from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import include
from django.urls import path

from main.views import splash_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', splash_page,  name='splash'),
    path(
        'about-me/',
        include(('aboutme.urls', 'aboutme'), namespace='about_me')
    ),
    path('', include(('blog.urls', 'blog'), namespace='blog')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
