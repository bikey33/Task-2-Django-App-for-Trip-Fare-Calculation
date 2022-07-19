from django.db import models
from django.urls import reverse
class Faredata(models.Model):
    # Making Datamodels to keep the given fare table in database
    time = models.IntegerField()
    # Storing various rates for different times of day
    service_charge = models.IntegerField()
    surge_charge = models.IntegerField()
    initial_fare = models.IntegerField()
    km_rate = models.IntegerField()
    def __str__(self):
        return str(self.time)
    # Providing default name representaion to each database entry

# Create your models here.
