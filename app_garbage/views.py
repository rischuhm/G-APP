from django.shortcuts import render
from django.http import HttpResponse
import folium, re

from .models import Entry

# Create your views here.

def index(request):
    return render(request,"index.html")


def muellmelden(request):
    lat = request.COOKIES.get("lat", 51.3396955)
    lon = request.COOKIES.get("lon", 12.3730747)

    m = folium.Map(location=[lat,lon],zoom_start=14,width="100%",height="100%", position="static")
      
    icon = folium.Icon(color="red")
    folium.Marker([lat, lon], draggable=True, icon=icon).add_to(m)
    
    m = m._repr_html_()
    m = re.search("<iframe.*</iframe>",m).group(0)
    m = re.sub("position:.*?;","position:static;",m)

    return render(request,"muellmelden.html",{"map":m})


def add_entry(request):
    ...


def findme(request):
    lat = 51.3396955
    lon = 12.3730747

    m = folium.Map(location=[lat,lon],zoom_start=14)

    tooltip ="Click ME!"
      
    folium.Marker([lat, lon], popup="<i>Blub</i>", tooltip=tooltip).add_to(m)
    
    m = m._repr_html_()


    return render(request,"index.html",{"map":m})


def show_entries(request):
    entries = Entry.objects.all()

    lat = request.COOKIES.get("lat", 51.3396955)
    lon = request.COOKIES.get("lon", 12.3730747)

    m = folium.Map(location=[lat,lon],zoom_start=14)

    for entry in entries: 
        folium.Marker([entry.lat,entry.lon]).add_to(m)

    m = m._repr_html_()

    return render(request, "entries.html", {"map":m})



