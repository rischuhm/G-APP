from django.shortcuts import render
from django.http import HttpResponse
import folium

# Create your views here.

def index(request):
    lat = request.COOKIES.get("lat", 51.3396955)
    lon = request.COOKIES.get("lon", 12.3730747)

    m = folium.Map(location=[lat,lon],zoom_start=14)
      
    folium.Marker([lat, lon], draggable=True).add_to(m)
    
    m = m._repr_html_()

    return render(request,"index.html",{"map":m})


def findme(request):
    lat = request.COOKIES.get("lat", 51.3396955)
    lon = request.COOKIES.get("lon", 12.3730747)

    m = folium.Map(location=[lat,lon],zoom_start=14)

    tooltip ="Click ME!"
      
    folium.Marker([lat, lon], popup="<i>Blub</i>", tooltip=tooltip).add_to(m)
    
    m = m._repr_html_()


    return render(request,"index.html",{"map":m})