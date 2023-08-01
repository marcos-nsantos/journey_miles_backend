from django.db import models


class Destiny(models.Model):
    name = models.CharField(max_length=150, blank=False)
    photo1 = models.ImageField(upload_to='destiny_photos', blank=True)
    photo2 = models.ImageField(upload_to='destiny_photos', blank=True)
    goal = models.CharField(max_length=160, blank=False)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
