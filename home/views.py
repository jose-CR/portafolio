from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.utils.translation import gettext as _
from django.views.generic import TemplateView
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from projects.models import Technology, Project
from .models import ContactMe, AboutPageConfig
from .forms import ContactMeForm

# Create your views here.
def app(request):
    button = _("Go")
    return render(request, 'index.html', {'button': button})

class About_Me(TemplateView):
    template_name = "about_me.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        projects = Project.objects.all()

        for project in projects:
            project.tech_ids = list(project.technologies.values_list('id', flat=True))
        
        try:
            config = AboutPageConfig.objects.select_related('featured_profile').get()
            profile = config.featured_profile
        except AboutPageConfig.DoesNotExist:
            profile = None

        context['projects'] = projects
        context['technologies'] = Technology.objects.all()
        context['profile'] = profile
        context['contact_me'] = ContactMeForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = ContactMeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about_me')
        else:
            context = self.get_context_data()
            context['contact_form'] = form
            return self.render_to_response(context)

class Contact_Me(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = ContactMe.objects.all()
        return context
    template_name = "contact_me.html"

@csrf_exempt
@require_POST
def mark_as_seen(request):
    contact_id = request.POST.get("id")
    try:
        contact = ContactMe.objects.get(id=contact_id)
        contact.active = False
        contact.save()
        return JsonResponse({"status":"ok"})
    except ContactMe.DoesNotExist:
        return JsonResponse({"status": "no found"}, status=404)

@csrf_exempt
def delete_contact_ajax(request):
    if request.method == 'POST':
        contact_id = request.POST.get('id')
        try:
            contact = ContactMe.objects.get(id=contact_id)
            contact.delete()
            return JsonResponse({'status': 'ok'})
        except ContactMe.DoesNotExist:
            return JsonResponse({'status': 'not_found'}, status=404)
    return JsonResponse({'status': 'invalid'}, status=400)
