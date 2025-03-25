from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project
from .forms import ProjectForm

# Create your views here.
def project(request):
    projects = Project.objects.all()
    
    return render(request, 'project.html', {'projects': projects})

def projectCreate(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            messages.success(request, 'Project created successfully!')
            return redirect('projectCreate')
        else:
            messages.error(request, 'There was an error creating the project. Please try again.')
    else:
        form = ProjectForm()
    return render(request, 'views/project/projectCreate.html', {'form': form})