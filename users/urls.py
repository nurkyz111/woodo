from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import register


urlpatterns = [
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
]