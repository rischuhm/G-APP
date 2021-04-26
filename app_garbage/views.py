from django.http.response import JsonResponse
from django.shortcuts import render,redirect
from django.core import serializers
from django.http import HttpResponse
import folium, re, datetime
from .models import Entry

# Create your views here.

def index(request):
    return render(request,"index.html")


def muellmelden(request):
    return render(request,"muellmelden.html")

def fetch(request):
    entries = serializers.serialize("json",Entry.objects.filter(date__gte=datetime.date.today()))
    return JsonResponse(entries, safe=False)


def add_entry(request):
    lat = request.POST.get("lat")
    lon = request.POST.get("lon")

    entry = Entry(lat=lat,lon=lon)
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



