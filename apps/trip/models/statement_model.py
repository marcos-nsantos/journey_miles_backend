from django.db import models


class Statement(models.Model):
    photo = models.ImageField(upload_to='statement_photos')
    text = models.TextField()
    person = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
