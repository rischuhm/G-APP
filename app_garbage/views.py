from django.http.response import JsonResponse
from django.shortcuts import render
from django.core import serializers
import folium, datetime
from .models import Garbage_Entry

# Create your views here.

def muellmelden(request):
    return render(request,"muellmelden.html")

def fetch():
    entries = serializers.serialize("json",Garbage_Entry.objects.filter(date__gte=datetime.date.today()))
    return JsonResponse(entries, safe=False)


def add_entry(request):
    lat = request.POST.get("lat")
    lon = request.POST.get("lon")

    entry = Garbage_Entry(lat=lat,lon=lon)
    entry.save()
    return render(request,"muellmelden.html")


def show_entries(request):
    entries = Entry.objects.all()

    lat = 51.3396955
    lon = 12.3730747

    m = folium.Map(location=[lat,lon],zoom_start=12)

    for entry in entries: 
        icon = folium.Icon(color="blue", icon="trash", prefix="glyphicon")
        folium.Marker([entry.lat,entry.lon], icon=icon).add_to(m)

    m = m._repr_html_()

    return render(request, "entries.html", {"map":m})



