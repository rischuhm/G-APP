from django.shortcuts import render,redirect
from django.http import HttpResponse
import folium, re, datetime

from .models import Entry

# Create your views here.

def index(request):
    return render(request,"index.html")


def muellmelden(request):
    entries = Entry.objects.filter(date__gte=datetime.date.today())
    
    lat =  51.3396955
    lon =  12.3730747



    m = folium.Map(location=[lat,lon],zoom_start=14,width="100%",height="100%")
      
    icon = folium.Icon(color="red", icon="trash", prefix="fa")
    folium.Marker([lat, lon], draggable=True, icon=icon).add_to(m)


    
    for entry in entries: 
        icon = folium.Icon(color="blue", icon="trash", prefix="fa", angle=10)
        folium.Marker([entry.lat,entry.lon], icon=icon).add_to(m)
    
    m = m._repr_html_()
    m = re.search("<iframe.*</iframe>",m).group(0)
    m = re.sub("position:.*?;","position:static;",m)
    marker_name = re.search("var%20(marker_.*?)%20",m).group(1)
    return render(request,"muellmelden.html",{"map":m, "marker_name":marker_name})


def add_entry(request):
    lat = request.POST.get("lat")
    lon = request.POST.get("lon")

    entry = Entry(lat=lat,lon=lon)
    entry.save()
    return redirect(muellmelden)


def show_entries(request):
    entries = Entry.objects.all()

    lat = 51.3396955
    lon = 12.3730747

    m = folium.Map(location=[lat,lon],zoom_start=12)

    for entry in entries: 
        folium.Marker([entry.lat,entry.lon]).add_to(m)

    m = m._repr_html_()

    return render(request, "entries.html", {"map":m})



