from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Salon)
class SalonAdmin(admin.ModelAdmin):
    list_display = ('nom', 'classe', 'date_add', 'status',)
    list_filter = ('status',)

    # Champs de recherche corrigé
    search_fields = ('projet', 'nom')

@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('auteur', 'message', 'salon', 'status',)
    list_filter = ('status',)

    # Champs de recherche corrigé
    search_fields = ('salon', 'nom')
