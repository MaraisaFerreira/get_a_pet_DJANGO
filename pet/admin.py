from django.contrib import admin
from .models import Pet


@admin.register(Pet)
class PetsAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'age', 'age_type',
                    'animal_type', 'available')
    list_display_links = ('name',)
    ordering = ('-created_at',)
