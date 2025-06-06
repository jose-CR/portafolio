from home.forms import CustomUserCreationForm, CustomUserChangeForm
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.views.generic import CreateView, UpdateView, DeleteView
from django.utils.translation import gettext as _
from home.models import UserProfile
from django.contrib.auth.decorators import login_required

# Create perfil
class ProfileCreateView(CreateView):
    model = UserProfile
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('app')

    def form_valid(self, form):
        self.object = form.save()
        success_url = reverse_lazy('app')
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(self.request, username=username, password=password)
        if user:
            login(self.request, user)
            
        return redirect(success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Register')
        context['contents'] = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'github', 'linkedin', 'description']
        context['content_button'] = _('Sing Up')
        return context

# Read perfil
class Profile():
    def exit(request):
        logout(request)
        return redirect('app')

    @login_required
    def index(request):

        context = {
            'label_username': _('username'),
            'label_first_name': _('First name'),
            'label_last_name': _('Last name'),
            'label_email': _('Email'),
            'label_description': _('description'),
            'label_github': ('Github'),
            'label_linkedin': ('Linkedin'),
        }

        return render(request, 'profile.html', context)
    
# Update perfil
class ProfileUpdateView(UpdateView):
    model = UserProfile
    form_class = CustomUserChangeForm
    template_name = 'profile/profile_edit.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        user_id = int(self.kwargs.get('pk'))
        if self.request.user.id == user_id:
            return self.request.user
        raise Http404("No puedes editar otro usuario.")

    def form_valid(self, form):
        messages.success(self.request, 'Tu perfil se ha actualizado correctamente.')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = _('Edit User')
        context['contents'] = ['username', 'first_name', 'last_name', 'email', 'github', 'linkedin', 'description']
        context['content_button'] = _('Edit')
        return context
    
# Delete perfil 
class ProfileDeleteView(DeleteView):
    model = UserProfile
    template_name = 'profile/profile_delete.html'
    success_url = reverse_lazy('app')

    def get_queryset(self):
        return UserProfile.objects.filter(pk=self.request.user.pk)

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        logout(request)

        return response
