from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from . import views

urlpatterns = [
    path('register', views.register, name="register"),
    path('login', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('account/<int:userID>/view_profile', views.viewProfile,name='viewProfile'),
    path('account/<int:userID>/edit_profile', views.viewProfile,name='editProfile'),
    # Here we have a list of employees page -> Should lead to their profile if clicked on
    path('agents/', views.agents, name='agents'),
    # Path leads to a single users in our system
    path('users/<int:userID>/', views.singleUser, name="users"),
    #path('users', include('users.urls')),
    #path('users', include('django.contrib.auth.urls')),
]