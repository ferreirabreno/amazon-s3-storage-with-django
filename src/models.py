from django.db import models

class File(models.Model):
    file = models.FileField(max_length=200)
    description = models.CharField(max_length=255, blank=True)