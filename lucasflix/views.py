
from django.shortcuts import render, redirect
from django.http import HttpResponse
from serie.models import Serie

def home(request):
    series = Serie.objects.all()

    return render(request, "home.html", {'series':series})