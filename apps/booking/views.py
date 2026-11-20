"""
booking/views.py
Calendar view, AJAX slot booking, and user dashboard.
"""

import json
import calendar
from datetime import date

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

from .models import Booking


def _build_calendar_events(month: int, year: int):
    """
    Return a dict mapping day → list of booked user emails for
    the given month/year.  Used to populate the calendar view.
    """
    month_name = date(year, month, 1).strftime('%B %Y')
    bookings = Booking.objects.filter(
        month_name=month_name
    ).select_related('user')

    events = {}
    for b in bookings:
        day = b.tdate
        events.setdefault(day, []).append(b.user.email)
    return events


@login_required
def booking_calendar_view(request):
    """
    Interactive booking calendar .
    Shows current month; days are clickable to book a slot via AJAX.
    """
    today = date.today()
    month = today.month
    year = today.year
    month_label = today.strftime('%B %Y')

    # Calendar grid metadata
    first_weekday, days_in_month = calendar.monthrange(year, month)
    # Python: Monday=0; JS/original used Sunday=0 — convert to Sunday-start
    first_weekday = (first_weekday + 1) % 7  # Mon→1 … Sun→0

    events = _build_calendar_events(month, year)

    # Build flat list of cells for the template
    cells = []
    for day_num in range(1, days_in_month + 1):
        day_events = events.get(day_num, [])
        from django.conf import settings
        max_slots = getattr(settings, 'MAX_SLOTS_PER_DAY', 3)
        cells.append({
            'day': day_num,
            'events': day_events,
            'is_past': day_num < today.day,
            'is_today': day_num == today.day,
            'is_full': len(day_events) >= max_slots,
            'user_booked': request.user.email in day_events,
        })

    context = {
        'month_label': month_label,
        'month': month,
        'year': year,
        'first_weekday': first_weekday,
        'days_in_month': days_in_month,
        'today_day': today.day,
        'cells': cells,
    }
    return render(request, 'booking/calendar.html', context)


@login_required
@require_POST
def book_slot_view(request):
    """
    AJAX endpoint to book a slot.
    Expects JSON body: { "date": <int day>, "month_name": <str "Month YYYY"> }
    Returns JSON: { "status": "success"|"error", "message": <str> }
    """
    try:
        data = json.loads(request.body)
        tdate = int(data.get('date', 0))
        month_name = data.get('month_name', '').strip()
    except (ValueError, KeyError, json.JSONDecodeError):
        return JsonResponse({'status': 'error', 'message': 'Invalid request data.'}, status=400)

    if not tdate or not month_name:
        return JsonResponse({'status': 'error', 'message': 'Missing date or month.'}, status=400)

    # Validate day is not in the past
    today = date.today()
    current_month_name = today.strftime('%B %Y')
    if month_name == current_month_name and tdate < today.day:
        return JsonResponse({'status': 'error', 'message': 'Cannot book a past date.'}, status=400)

    # Check duplicate booking for this user
    if Booking.user_already_booked(request.user, tdate, month_name):
        return JsonResponse({
            'status': 'error',
            'message': f'You have already booked on day {tdate} of {month_name}.'
        }, status=400)

    # Check if slot is full (max 3 per day)
    if Booking.is_slot_full(tdate, month_name):
        return JsonResponse({
            'status': 'error',
            'message': f'Slot is full for {tdate} {month_name}. No more bookings available.'
        }, status=400)

    # Create booking
    booking = Booking.objects.create(
        user=request.user,
        tdate=tdate,
        month_name=month_name
    )

    return JsonResponse({
        'status': 'success',
        'message': f'Booking confirmed for {tdate} {month_name}!',
        'booking_id': booking.pk,
    })


@login_required
def dashboard_view(request):
    """
    User dashboard showing all bookings .
    """
    user_bookings = Booking.objects.filter(user=request.user).order_by('-booked_at')

    try:
        profile = request.user.profile
    except Exception:
        profile = None

    context = {
        'bookings': user_bookings,
        'profile': profile,
        'total_bookings': user_bookings.count(),
    }
    return render(request, 'booking/dashboard.html', context)


@login_required
def cancel_booking_view(request, booking_id):
    """Cancel a user's own booking."""
    try:
        booking = Booking.objects.get(pk=booking_id, user=request.user)
        booking.delete()
        messages.success(request, 'Booking cancelled successfully.')
    except Booking.DoesNotExist:
        messages.error(request, 'Booking not found.')
    return redirect('booking:dashboard')
