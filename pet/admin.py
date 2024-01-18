from django.contrib import admin
from .models import Pet, PetImages


@admin.register(Pet)
class PetsAdmin(admin.ModelAdmin):
    list_display = ('name', 'color', 'age', 'age_type',
                    'animal_type', 'available')
    list_display_links = ('name',)
    ordering = ('-created_at',)


@admin.register(PetImages)
class PetImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'pet')
