from django.contrib.auth.models import User
from django.db import models

class Phone(models.Model):
    name = models.CharField(max_length=255)
    manufacturer = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    storage = models.CharField(max_length=255)
    used = models.BooleanField()
    price = models.FloatField(default=0.0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/", null=True, blank=True)
    location = models.ImageField(upload_to="locations/", null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.manufacturer}"


