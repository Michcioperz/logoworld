from colorful.fields import RGBColorField
from django.conf import settings
from django.db import models
from django.utils import timezone


class Spot(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="spots")
    latitude = models.FloatField()
    longitude = models.FloatField()
    created = models.DateTimeField(default=timezone.now)
    colour = RGBColorField(default="#FFFFFF")
