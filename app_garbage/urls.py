
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index" ),
    path('muellmelden', views.muellmelden, name="muellmelden" ),
    path('eintraege', views.show_entries, name="eintraege" ),
    path('neuer_eintrag', views.add_entry, name="eintraege" ),
]
