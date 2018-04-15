from django.db import models


class Key(models.Model):
    name = models.CharField(max_length=255)
    api_key = models.CharField(max_length=255)

    def __str__(self):
        return self.name
