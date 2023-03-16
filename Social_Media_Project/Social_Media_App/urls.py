from django.urls import path,include
from Social_Media_App import views
urlpatterns = [
    path('',views.Login, name='login'),
    path('register', views.Register, name='register'),
    path('logout',views.logout, name='logout'),
    path('home', views.Home, name='home'),
    path('login', views.Login, name='login'),
    path('profile',views.Profile, name='profile'),
    path('post', views.Post, name='post'),

]
