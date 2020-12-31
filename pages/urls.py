from django.urls import path
from .views import HomePageView, AboutPageView, contactView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', contactView, name='contact'),
]