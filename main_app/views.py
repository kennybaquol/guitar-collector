from django.shortcuts import render

# Add the Cat class & list and view function below the imports
class Guitar:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, brand, model):
    self.name = name
    self.brand = brand
    self.model = model

guitars = [
  Guitar("'60s Electric Guitar - Bourbon Burst", 'Gibson', 'Les Paul Standard')
]

# View functions
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def guitars_index(request):
    return render(request, 'guitars/index.html', { 'guitars' : guitars})