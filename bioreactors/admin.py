from django.contrib import admin
from .models import BioreactorUnit, AlgaeSpecies, Equipment

# Register your models here.

admin.site.register(BioreactorUnit)
admin.site.register(AlgaeSpecies)
admin.site.register(Equipment)