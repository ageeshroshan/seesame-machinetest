from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('posts/', views.posts, name='posts'),
    path('createpost/', views.createpost, name='createpost')
]
