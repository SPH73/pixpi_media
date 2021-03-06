"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from accounts.views import UserViewSet, GroupViewSet


router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

admin.site.site_header = "Esse Admin"
admin.site.site_title = "Esse Admin Portal"
admin.site.index_title = "Welcome to Esse Portal"

handler404 = 'config.views.handler404'
handler500 = 'config.views.handler500'

urlpatterns = [
    path('backoffice/', admin.site.urls),
  
    path('accounts/', include('allauth.urls')),
    
    
    path('', include('pages.urls')),
    
    path('profiles/', include('profiles.urls', namespace='profiles')),
    
    path('albums/', include('albums.urls', namespace='albums')),
    
    path('donations/', include('donations.urls', namespace='donations')),

    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
