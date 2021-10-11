from django.db import models

# Create your models here.

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)

    def __str__(self):
        return self.name