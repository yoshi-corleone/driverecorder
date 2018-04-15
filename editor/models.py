from django.db import models

from recorder.models import Point


class Course(models.Model):
    name = models.CharField(max_length=255)
    points = models.ManyToManyField(Point)

    def __str__(self):
        return self.name
