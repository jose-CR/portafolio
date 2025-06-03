from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Technology
from .forms import CreationTecnologiesForm, EditTechnologiesForm
from django.urls import reverse_lazy

# Create your views here.

class CreateTechnolgies(CreateView):
    model = Technology
    form_class = CreationTecnologiesForm
    success_url = reverse_lazy('read_tech')

    template_name = "technologies/create_tech.html"

class ReadTechnolgies(ListView):
    model = Technology
    context_object_name = "technologies"
    template_name = "tech.html"

class UpdateTechnologies(UpdateView):
    model = Technology
    form_class = EditTechnologiesForm
    template_name = "technologies/edit_tech.html"
    success_url = reverse_lazy('read_tech')

class DeleteTechnologies(DeleteView):
    model = Technology
    template_name = "technologies/delete_tech.html"
    success_url = reverse_lazy('read_tech')


