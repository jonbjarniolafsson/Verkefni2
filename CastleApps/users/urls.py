from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from . import views

urlpatterns = [
    path('register', views.register, name="register"),
    path('login', LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),

    #path('users', include('users.urls')),
    #path('users', include('django.contrib.auth.urls')),
]