from unicodedata import name
from django.db import models
from django.db.models import JSONField


class FormData(models.Model):
    name = models.CharField(max_length=50)
    data = JSONField()

    def __str__(self):
        return self.name