from django.shortcuts import render
from django.utils.translation import gettext as _
from django.views.generic import TemplateView
from projects.models import Technology, Project

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

        context['projects'] = projects
        context['technologies'] = Technology.objects.all()
        context['profile'] = self.request.user
        return context