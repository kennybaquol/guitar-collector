from django.forms import ModelForm
from .models import Tuned

class TunedForm(ModelForm):
  class Meta:
    model = Tuned
    fields = ['date', 'tuning']