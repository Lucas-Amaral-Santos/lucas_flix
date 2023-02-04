from django.forms import ModelForm, ModelChoiceField, CharField, ChoiceField
from .models import Serie, Temporada, Episodio

class SerieForm(ModelForm):

    class Meta:
        model = Serie
        fields = '__all__'
        exclude = ['slug', 'dt_cadastro']

class TemporadaForm(ModelForm):

    def __init__(self, serie_choice=None):
        super(TemporadaForm, self).__init__()
        if serie_choice is not None:
            serie_choice = Serie.objects.filter(slug=serie_choice)
            self.fields['serie'] =  ModelChoiceField(queryset=serie_choice)
    
    class Meta:
        model = Temporada
        fields = '__all__'
        exclude = ['slug', 'dt_cadastro']

class EpisodioForm(ModelForm):

    def __init__(self, serie_choice=None):
        super(EpisodioForm, self).__init__()
        if serie_choice is not None:
            temporada_choice = Temporada.objects.filter(serie__id=serie_choice)
            serie_choice = Serie.objects.filter(slug=serie_choice)
            self.fields['serie'] =  ModelChoiceField(queryset=serie_choice)
            self.fields['temporada'] =  ModelChoiceField(queryset=temporada_choice)

    class Meta:
        model = Episodio
        fields = '__all__'
        exclude = ['slug', 'dt_cadastro']