from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_name', 'project_description', 'project_image_url']
        
        project_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter project name'}))
        
        project_description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter project description'}))
        
        project_image_url = forms.CharField(widget=forms.ClearableFileInput(attrs={'placeholder': 'Choose project image'}))