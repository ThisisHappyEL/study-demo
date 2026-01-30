from django.shortcuts import render
from .models import FrogAquarium
from .forms import FrogAquariumForm

def aquarium_list(request):
    aquariums = FrogAquarium.objects.all()
    return render(request, 'listings.html', {'aquariums': aquariums})

def create_aquarium(request):
    if request.method == 'POST':
        form = FrogAquariumForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('aquarium_list_url')
    else:
        form = FrogAquariumForm()
    
    return render(request, 'aquarium_create.html', {'form': form})