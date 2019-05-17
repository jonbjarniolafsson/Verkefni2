from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name="register"),
    path('login', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('<int:userID>/view_profile', views.viewProfile, name='viewProfile'),
    path('<int:userID>/edit_profile', views.editProfile, name='editProfile'),
    path('<int:userID>/view_history', views.viewHistory, name='view_history'),
    # Here we have a list of employees page -> Should lead to their profile if clicked on
    path('agents/', views.agents, name='agents'),
    # Path leads to a single users in our system
    path('<int:userID>/', views.singleUser, name="users"),
    path('contact-us', views.contactUs, name="contact_us"),
    # path('users', include('users.urls')),
    # path('users', include('django.contrib.auth.urls')),
    path('<int:userID>/owned_apartments', views.ownedApartments, name="owned_apartments"),
    path('users/<int:userID>/managed_apartments', views.managedApartments, name="managed_apartments"),
]
