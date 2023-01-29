from django.contrib import admin
from .models import Species, Category, Size, Enviroment
# Register your models here.


class SpeciesAdmin(admin.ModelAdmin):
    model = Species
    list_display = [
        'name',
        'slug',
        'latin_name',
        'description',
        'dangerous_species',
        'category',
        'size',
        'enviroment',
    ]


admin.site.register(Species, SpeciesAdmin)
admin.site.register(Enviroment)
admin.site.register(Size)
admin.site.register(Category)
