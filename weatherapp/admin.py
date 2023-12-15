from django.contrib import admin
from .models import contact

@admin.register(contact)
class contactAdmin(admin.ModelAdmin):
    pass