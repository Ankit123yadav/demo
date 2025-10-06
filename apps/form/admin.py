from django.contrib import admin

from.models import Registration
from.models import Contactus

from django import forms
# Register your models here.
from .models import WorkshopRegistration

admin.site.register(WorkshopRegistration)

admin.site.register(Registration)
admin.site.register(Contactus)