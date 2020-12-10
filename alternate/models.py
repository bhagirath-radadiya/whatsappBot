from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.

class Alternate(models.Model):
    incomingMsg = models.CharField(max_length=500)
    reply = JSONField()