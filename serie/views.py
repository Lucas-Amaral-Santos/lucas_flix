from django.shortcuts import render, redirect
from .forms import SerieForm, TemporadaForm, EpisodioForm
from .models import Serie, Temporada, Episodio

def detalhes_serie(request, serie):
    serie = Serie.objects.get(id=serie)
    temporadas = Temporada.objects.filter(serie=serie.id)
    episodios = Episodio.objects.filter(serie=serie.id)

    return render(request, 'detalhes_serie.html', {'serie': serie, 'temporadas':temporadas, 'episodios':episodios})

def cadastra_serie(request):
    form_serie = SerieForm()
    new_serie = None

    if request.method == 'POST':
        form_serie = SerieForm(request.POST, request.FILES)
        if (form_serie.is_valid()):
            new_serie = Serie.objects.create(
                titulo = form_serie.cleaned_data['titulo'],
                descricao = form_serie.cleaned_data['descricao'],
                capa = form_serie.cleaned_data['capa'],
            )
            new_serie.save()
            return redirect('serie:detalhes_serie', new_serie.id)

    return render(request, 'cadastra_serie.html', {'form': form_serie})

def cadastra_temporada(request):
    form_temporada = TemporadaForm()

    if request.method == 'POST':
        form_temporada = TemporadaForm(request.POST)
        if (form_temporada.is_valid()):
            new_temporada = Temporada.objects.create(
                temporada = form_temporada.cleaned_data['temporada'],
                serie = form_temporada.cleaned_data['serie'],
            )
            new_temporada.save()
            return redirect('serie:detalhes_serie', new_temporada.serie.id)

    return render(request, 'cadastra_serie.html', {'form': form_temporada})


def cadastra_episodio(request, serie):
    form_episodio = EpisodioForm(serie_choice=serie)
    
    if request.method == 'POST':
        form_episodio = EpisodioForm(request.POST, request.FILES)
        if (form_episodio.is_valid()):
            new_episodio = Episodio.objects.create(
                numero = form_episodio.cleaned_data['numero'],
                nome = form_episodio.cleaned_data['nome'],
                video = form_episodio.cleaned_data['video'],
                serie = form_episodio.cleaned_data['serie'],
                temporada = form_episodio.cleaned_data['temporada'],
            )
            new_episodio.save()
            return redirect('serie:detalhes_serie', new_episodio.serie.id)

    return render(request, 'cadastra_serie.html', {'form': form_episodio})

def detalhes_episodio(request, episodio):
    episodio = Episodio.objects.get(id=episodio)

    return render(request, 'detalhes_episodio.html', {'episodio':episodio})