from django.db import models

# Create your models here.

class Order(models.Model):
    name = models.CharField(max_length=255)
    order = models.JSONField(null = True)
    phone_number = models.CharField(max_length=255)
    