from django.urls import path, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('indexpage/', views.IndexPageView.as_view() , name='indexpage')
    # path('indexpage', TemplateView.as_view(template_name = 'indexpage.html'))
]