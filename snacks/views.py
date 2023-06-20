from django.shortcuts import render

# Create your views here.

from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Snack


class SnackListView(ListView):
    template_name='snacks_list.html'
    model = Snack

class SnackDetailView(DetailView):
    template_name="snacks_detail.html"
    model= Snack

class SnackCreateView(CreateView):
    template_name='snack_create.html'
    model=Snack
    fields= ['title', 'purchaser', 'description'] # my form feilds

class SnackUpdateView(UpdateView):
    template_name='snack_update.html'
    model=Snack
    fields="__all__"
    success_url=reverse_lazy('snacks_list') #to redrect user to snacks_list page after update

class SnackDeleteView(DeleteView):
    template_name='snack_delete.html'
    model=Snack
    success_url=reverse_lazy('snacks_list')