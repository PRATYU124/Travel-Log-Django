# Create your views here.
from django.shortcuts import render, redirect
from .models import Trip, Expense,Destination
from django.contrib.auth.decorators import login_required
import json
from django.core.serializers import serialize
from django.shortcuts import render, get_object_or_404


def dashboard(request):
    trips = Trip.objects.all()
    return render(request, 'dashboard.html', {'trips': trips})



@login_required
def create_trip(request):
    if request.method == "POST":
        title = request.POST['title']
        description = request.POST['description']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        Trip.objects.create(user=request.user, title=title, description=description, start_date=start_date, end_date=end_date)
        return redirect('dashboard')
    return render(request, 'create_trip.html')


def trip_map(request, trip_id):
    trip = Trip.objects.get(id=trip_id)
    destinations = Destination.objects.filter(trip=trip)

    total_price = None
    if request.method == 'POST':
        price = float(request.POST.get('price', 0))
        nights = int(request.POST.get('nights', 0))
        total_price = round(price * nights, 2)

    destinations_json = json.dumps([
        {"latitude": d.latitude, "longitude": d.longitude, "name": d.name, "description": d.description}
        for d in destinations
    ])

    return render(request, 'trip_map.html', {
        'trip': trip,
        'destinations_json': destinations_json,
        'total_price': total_price
    })
