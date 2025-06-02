from django.shortcuts import render
from django.utils.translation import gettext as _

# Create your views here.
def app(request):
    button = _("Go")
    return render(request, 'index.html', {'button': button})