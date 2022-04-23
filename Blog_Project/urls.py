
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path,include
from django.conf import settings
from django.contrib.staticfiles.urls import static,staticfiles_urlpatterns
from django.views.static import serve

from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('App_Login.urls')),
    path('blog/',include('App_Blog.urls')),
    path('', views.index,name = 'index'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
