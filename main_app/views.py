from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Guitar, Player
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
  # Get the players the guitar doesn't have...
  # First, create a list of the player ids that the guitar DOES have
  id_list = guitar.players.all().values_list('id')
  # Now we can query for toys whose ids are not in the list using exclude
  players_guitar_doesnt_have = Player.objects.exclude(id__in=id_list)

  tuned_form = TunedForm()
  return render(request, 'guitars/detail.html', { 
    'guitar': guitar,
    'tuned_form': tuned_form,
    'players': players_guitar_doesnt_have
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

def assoc_player(request, guitar_id, player_id):
  # Note that you can pass a player's id instead of the whole player object
  Guitar.objects.get(id=guitar_id).players.add(player_id)
  return redirect('detail', guitar_id=guitar_id)

class GuitarCreate(CreateView):
  model = Guitar
  fields = ['brand', 'model', 'color']
  success_url = '/guitars/'

class GuitarUpdate(UpdateView):
  model = Guitar
  fields = '__all__'

class GuitarDelete(DeleteView):
  model = Guitar
  success_url = '/guitars/'

class PlayerList(ListView):
  model = Player

class PlayerDetail(DetailView):
  model = Player

class PlayerCreate(CreateView):
  model = Player
  fields = '__all__'

class PlayerUpdate(UpdateView):
  model = Player
  fields = ['name', 'band']

class PlayerDelete(DeleteView):
  model = Player
  success_url = '/players/'