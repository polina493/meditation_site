from django.urls import path
from . import views
from .views import signup  
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('meditations/', views.meditations, name='meditations'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
]
