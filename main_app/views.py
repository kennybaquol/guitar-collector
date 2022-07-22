from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Guitar
from .forms import TunedForm

# View functions
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def guitars_index(request):
  guitars = Guitar.objects.all()
  return render(request, 'guitars/index.html', { 'guitars' : guitars})

def guitars_detail(request, guitar_id):
  guitar = Guitar.objects.get(id=guitar_id)
  tuned_form = TunedForm()
  return render(request, 'guitars/detail.html', { 
    'guitar': guitar,
    'tuned_form': tuned_form 
    })

def add_tuned(request, guitar_id):
  # create a ModelForm instance using the data in request.POST
  form = TunedForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the guitar_id assigned
    new_tuned = form.save(commit=False)
    new_tuned.guitar_id = guitar_id
    new_tuned.save()
  return redirect('detail', guitar_id=guitar_id)

class GuitarCreate(CreateView):
  model = Guitar
  fields = '__all__'
  success_url = '/guitars/'

class GuitarUpdate(UpdateView):
  model = Guitar
  fields = '__all__'

class GuitarDelete(DeleteView):
  model = Guitar
  success_url = '/guitars/'