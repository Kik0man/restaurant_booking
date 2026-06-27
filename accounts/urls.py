from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('booking/<int:pk>/edit/', views.BookingUpdateView.as_view(), name='booking_edit'),
    path('booking/<int:pk>/delete/', views.BookingDeleteView.as_view(), name='booking_delete'),
    path('register/', views.register_view, name='register'),
]