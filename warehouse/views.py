from dataclasses import field
import imp
from pyexpat import model
from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Items

# Create your views here.

class ItemList(ListView):
    model = Items
    context_object_name = 'items'
    template_name = 'warehouse/home.html'

class ItemDetail(DetailView):
    model = Items
    context_object_name = 'items'
    template_name = 'warehouse/detail.html'

class ItemCreate(CreateView):
    model = Items
    template_name = 'warehouse/create.html'
    # field = ['item','house_no']
    fields = '__all__'
    success_url = reverse_lazy('home')