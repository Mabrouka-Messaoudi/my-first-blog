from django.urls import path
from . import views



urlpatterns = [
     # Root URL now shows the blog page
    path('', views.blog , name='blog'),
    
    
]