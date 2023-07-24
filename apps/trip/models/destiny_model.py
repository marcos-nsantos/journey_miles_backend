from django.db import models


class Destiny(models.Model):
    photo = models.ImageField(upload_to='destiny_photos', blank=True)
    name = models.CharField(max_length=150, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
