from django.db import models

# Create your models here.
class Guitar(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.TextField(max_length=250)

    def __str__(self):
        return self.brand