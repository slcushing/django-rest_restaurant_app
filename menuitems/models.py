from django.db import models

# Create your models here.

class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null=True)
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.name