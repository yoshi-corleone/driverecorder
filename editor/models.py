from django.db import models
from django.contrib.auth.models import User

from recorder.models import Point


class Course(models.Model):
    name = models.CharField(max_length=255)
    points = models.ManyToManyField(Point)
    # user = models.ForeignKey(User)

    def __str__(self):
        return self.name
