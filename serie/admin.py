from django.contrib import admin
from .models import Serie, Temporada, Episodio

@admin.register(Serie)
class SerieAdmin(admin.ModelAdmin):
    pass


@admin.register(Temporada)
class TemporadaAdmin(admin.ModelAdmin):
    pass

@admin.register(Episodio)
class EpisodioAdmin(admin.ModelAdmin):
    pass