"""jobBoard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from vacancy import views as top_page_views

# Customize Admin Interface
admin.site.site_header = 'Job Board Admin'
admin.site.site_title = 'Job Board'
admin.site.index_title = 'Job Board '

urlpatterns = [
    path('admin/', admin.site.urls),
    # urls handling WYSIWYG editor
    path('editor/', include('django_summernote.urls')),
    # Landing Page URL
    path('', top_page_views.landing_page, name='landing_page'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)










