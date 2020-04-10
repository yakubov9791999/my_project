from django.urls import path
from . import views

urlpatterns = [
    path('', views.pizza, name='home'),
    path('<pizza_id>', views.pizza_detail, name='pizza-detail' )
]
