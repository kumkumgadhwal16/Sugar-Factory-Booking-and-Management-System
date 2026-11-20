"""Sugar Factory Booking System — Root URL Configuration"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Django Admin
    path('admin/', admin.site.urls),

    # Core (homepage, about, products, manufacturing pages)
    path('', include('apps.core.urls')),

    # User Accounts (register, login, logout, profile)
    path('accounts/', include('apps.accounts.urls')),

    # Booking (calendar, book slot, dashboard)
    path('booking/', include('apps.booking.urls')),

    # Manufacturing process pages
    path('manufacturing/', include('apps.manufacturing.urls')),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
