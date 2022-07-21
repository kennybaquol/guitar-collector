from django.db import models
from django.urls import reverse

# Create your models here.
class Guitar(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.TextField(max_length=250)

    def __str__(self):
        return self.brand

    def get_absolute_url(self):
        return reverse('detail', kwargs={'guitar_id': self.id})

class TunedTo(models.Model):
    date = models.DateField()
    tuning = models.CharField(max_length=8)

    guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE)

    def __str__(self):
        # return f"{self.get_tuning_display()} on {self.date}"
        return self.tuning