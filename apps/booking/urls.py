"""booking/urls.py"""

from django.urls import path
from . import views

app_name = 'booking'

urlpatterns = [
    path('calendar/', views.booking_calendar_view, name='calendar'),
    path('book/', views.book_slot_view, name='book_slot'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('cancel/<int:booking_id>/', views.cancel_booking_view, name='cancel'),
]
