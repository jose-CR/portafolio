from django import forms
from .models import Project, Technology

class CreationProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = [
            'name', 'description', 'image_project', 'technologies'
        ]

class CreationTecnologiesForm(forms.ModelForm):
    class Meta:
        model = Technology
        fields = [
            'name', 'image_technology'
        ]

class EditTechnologiesForm(forms.ModelForm):
    class Meta:
        model = Technology
        fields = [
            'name', 'image_technology'
        ]
