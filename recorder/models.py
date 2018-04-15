from django.db import models
from datetime import datetime


class Picture(models.Model):
    file_name = models.CharField(max_length=255)
    upload_time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.file_name


class Point(models.Model):
    picture = models.OneToOneField(Picture, related_name='picture', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    longitude = models.DecimalField(max_digits=11, decimal_places=8, blank=True, null=True)
    time = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
