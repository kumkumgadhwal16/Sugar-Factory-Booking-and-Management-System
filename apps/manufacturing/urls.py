"""manufacturing/urls.py"""

from django.urls import path
from . import views

app_name = 'manufacturing'

urlpatterns = [
    path('', views.manufacturing_overview_view, name='overview'),
    path('<slug:slug>/', views.manufacturing_stage_view, name='stage_detail'),
]
