from django.contrib import admin

from.models import Registration
from.models import Contactus

from django import forms
# Register your models here.

admin.site.register(Registration)
admin.site.register(Contactus)