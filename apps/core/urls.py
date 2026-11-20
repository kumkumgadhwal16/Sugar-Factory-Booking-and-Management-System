"""core/urls.py"""

from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('manager/', views.manager_view, name='manager'),
    path('performance/', views.performance_view, name='performance'),
    path('products/', views.our_products_view, name='products'),
]
