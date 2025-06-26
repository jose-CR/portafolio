from django.contrib import admin
from .models import UserProfile, ContactMe, AboutPageConfig

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(ContactMe)
admin.site.register(AboutPageConfig)