from django.urls import path
from .views import CreateTechnolgies, ReadTechnolgies, UpdateTechnologies, DeleteTechnologies, ReadProjects, CreateProjects, UpdateProject, DeleteProject

urlpatterns = [
    path('technologies/', ReadTechnolgies.as_view(), name="read_tech"),
    path('technologies/create', CreateTechnolgies.as_view(), name="create_tech"),
    path('technologies/edit/<int:pk>', UpdateTechnologies.as_view(), name="edit_tech"),
    path('technologies/delete/<int:pk>', DeleteTechnologies.as_view(), name="delete_tech"),

    path('', ReadProjects.as_view(), name="read_project"),
    path('create/', CreateProjects.as_view(), name="create_project"),
    path('edit/<int:pk>', UpdateProject.as_view(), name="edit_project"),
    path('delete/<int:pk>', DeleteProject.as_view(), name="delete_project"),
]