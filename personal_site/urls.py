from django.contrib import admin
from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about-me/', include(('aboutme.urls', 'aboutme'), namespace='about_me')),
    path('blog/', include(('blog.urls', 'blog'), namespace='blog')),
]
