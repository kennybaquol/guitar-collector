from django.db import models
from django.urls import reverse

TUNINGS = (
    ('EADGBE', 'Standard'),
    ('DADGBE', 'Drop D'),
    ('EbAbDbGbBbEb', 'Half Step Down'),
    ('DADGAD', 'Dad Gad')
)

class Player(models.Model):
  name = models.CharField(max_length=50)
  band = models.CharField(max_length=50)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('players_detail', kwargs={'pk': self.id})

# Create your models here.
class Guitar(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.TextField(max_length=250)

    def __str__(self):
        return self.brand

    def get_absolute_url(self):
        return reverse('detail', kwargs={'guitar_id': self.id})

class Tuned(models.Model):
    date = models.DateField('Tuning Date')
    tuning = models.CharField(
        max_length=24,
        choices=TUNINGS,
        default=TUNINGS[0][0]
        )

    guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_tuning_display()} on {self.date}"

    # change the default sort
    class Meta:
        ordering = ['-date']
