from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Pizza
from .forms import OrderForm

# Create your views here.

def home(request):
    pizzas = Pizza.objects.all()
    return render(request, 'index.html', {
        'pizzas': pizzas,
    })

def pizza_detail(request, pizza_id):
    pizza = get_object_or_404(Pizza, id=pizza_id)
    form = OrderForm(request.POST or None, initial=
        {'pizza': pizza}
    )
    if request.method == 'POST':
        if form.is_valid():
            form.save()
    return render(request, 'pizza_detail.html', {
        'pizza': pizza,
        'form': form,
    })

