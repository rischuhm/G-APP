from django.db import models

# Create your models here.

class Garbage_Entry(models.Model):
    lat = models.CharField(max_length=100, default="")
    lon = models.CharField(max_length=100, default="")
    date = models.DateTimeField(auto_now=True)

   
    def __str__(self):
        return f"{self.id} {self.date}"