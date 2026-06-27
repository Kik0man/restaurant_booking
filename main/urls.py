from django.urls import path
from . import views

app_name = 'main'
urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('background.css', views.background_css, name='background_css'),
]