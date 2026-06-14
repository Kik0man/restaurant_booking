from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import custom_logout
from django.contrib import admin

admin.site.index_title = "Добро пожаловать"
admin.site.site_header = "Управление рестораном"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('booking/', include('bookings.urls')),
    path('accounts/', include('accounts.urls')),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('logout/', custom_logout, name='logout'),
]

# Раздача статических и медиа-файлов в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)