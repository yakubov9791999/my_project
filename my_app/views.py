from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse

from .models import Pizza
from .forms import OrderForm
from django.http import HttpResponseRedirect

# Create your views here.

def home(request):
    pizzas = Pizza.objects.all()

    return render(request, 'index.html', {
        'pizzas': pizzas,
    })

def pizza_detail(request, pizza_id):
    pizza = get_object_or_404(Pizza, id=pizza_id)

    form = OrderForm(request.POST or None, initial={
        'pizza':pizza
    })

    if form.is_valid():
        if request.method == 'POST':
            form.save()
            print(pizza.id)
            return HttpResponseRedirect(reverse('pizza', args=[pizza_id]))

    return render(request, 'pizza.html', {
        'pizza': pizza,
        'form': form,
    })

