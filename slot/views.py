from django.shortcuts import render, redirect
from .models import SlotBooking
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == "POST":
        return redirect('welcome')

    return render(request, 'login.html')

def signup_view(request):
    if request.method == "POST":
        return redirect('login')
    return render(request, 'signup.html')

def welcome_view(request):
    return render(request, 'slots/welcome.html')


def select_slot_view(request):
    if request.method == 'POST':
        selected_date = request.POST.get('selected_date')
        selected_time = request.POST.get('slot_time')
        return redirect('booking_details')
    return render(request, 'slots/select_slot.html')


def booking_details_view(request):
    if request.method == 'POST':
        # Handle form data here if needed
        return redirect('booking_confirmed')  # Step 4 page
    return render(request, 'slots/booking_details.html')


def booking_confirmed_view(request):
    selected_date = request.GET.get('selected_date')
    selected_slot = request.GET.get('selected_slot')
    selected_package = request.GET.get('selected_package')
    booking_id = "BD45678"  # You can generate dynamically if needed

    return render(request, 'slots/booking_confirmed.html', {
        'selected_date': selected_date,
        'selected_slot': selected_slot,
        'selected_package': selected_package,
        'booking_id': booking_id,
    })


def slot_submit_view(request):
    if request.method == "POST":
        selected_date = request.POST.get('selected_date')
        selected_slot = request.POST.get('slot')
        selected_package = request.POST.get('package')

        return redirect(
            f"/booking_confirmed/?selected_date={selected_date}&selected_slot={selected_slot}&selected_package={selected_package}"
        )






