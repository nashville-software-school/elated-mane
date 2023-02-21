"""Equipment class module"""
from django.db import models
from django.conf import settings


class Equipment(models.Model):
    """Equipment model class"""
    stylist = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    prepaid = models.BooleanField(default=False)
    appointment_date = models.DateField(auto_now=False, auto_now_add=False)
