from django.shortcuts import render
from django.http import HttpResponse
from .models import Pizza

# Create your views here.

def home(request):
    pizzas = Pizza.objects.all()

    return render(request, 'index.html', {
        'pizzas': pizzas,
    })

