from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Technology, Project
from .forms import CreationTecnologiesForm, EditTechnologiesForm, CreationProjectForm, EditProjectForm
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
    success_url = reverse_lazy('read_tech')
    template_name = "technologies/edit_tech.html"

class DeleteTechnologies(DeleteView):
    model = Technology
    success_url = reverse_lazy('read_tech')
    template_name = "technologies/delete_tech.html"

class CreateProjects(CreateView):
    model = Project
    form_class = CreationProjectForm
    success_url = reverse_lazy('read_project')

    template_name = "project/create_project.html"

class ReadProjects(ListView):
    model = Project
    context_object_name = "projects"
    template_name = "project.html"

class UpdateProject(UpdateView):
    model = Project
    form_class = EditProjectForm
    success_url = reverse_lazy('read_project')
    template_name = "project/edit_project.html"

class DeleteProject(DeleteView):
    model = Project
    success_url = reverse_lazy('read_project')
    template_name = "project/delete_project.html"
