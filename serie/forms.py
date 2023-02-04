from django.forms import ModelForm, ModelChoiceField, ChoiceField
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

    def __init__(self, serie_choice=None):
        super(EpisodioForm, self).__init__()
        serie_choice = Temporada.objects.filter(serie__id=serie_choice)
        self.fields['temporada'] =  ModelChoiceField(queryset=serie_choice)

    class Meta:
        model = Episodio
        fields = '__all__'
        exclude = ['slug', 'dt_cadastro']