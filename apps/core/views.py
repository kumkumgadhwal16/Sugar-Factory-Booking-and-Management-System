"""
core/views.py
Public-facing pages: home, about, products, contact, manager, performance.
"""

from django.shortcuts import render
from .models import AboutUs, ContactInfo, Manager, PerformanceData


def home_view(request):
    """Homepage with product cards and manufacturing carousel."""
    return render(request, 'core/home.html')


def about_view(request):
    """About Us overview page."""
    about = AboutUs.objects.first()
    return render(request, 'core/about.html', {'about': about})


def contact_view(request):
    """Contact Info page."""
    contact = ContactInfo.objects.first()
    return render(request, 'core/contact.html', {'contact': contact})


def manager_view(request):
    """Manager listing page ."""
    managers = Manager.objects.all()
    return render(request, 'core/manager.html', {'managers': managers})


def performance_view(request):
    """Performance data page."""
    data = PerformanceData.objects.all()
    return render(request, 'core/performance.html', {'performance_data': data})


def our_products_view(request):
    """Our Products page ."""
    return render(request, 'core/products.html')
