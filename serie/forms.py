from django.forms import ModelForm, ModelChoiceField, CharField, ChoiceField
from .models import Serie, Temporada, Episodio

class SerieForm(ModelForm):

    class Meta:
        model = Serie
        fields = '__all__'
        exclude = ['slug', 'dt_cadastro']

class TemporadaForm(ModelForm):
    
    class Meta:
        model = Temporada
        fields = '__all__'
        exclude = ['slug', 'dt_cadastro']

class EpisodioForm(ModelForm):

    class Meta:
        model = Episodio
        fields = '__all__'
        exclude = ['slug', 'dt_cadastro']