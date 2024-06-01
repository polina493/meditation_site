from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('meditations/', views.meditations, name='meditations'),
]
