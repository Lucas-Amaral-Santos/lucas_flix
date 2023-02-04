from django.db import models
from django.utils.text import slugify

class Serie(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    capa = models.ImageField(upload_to='images') 

    slug = models.SlugField()
    dt_cadastro = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
            self.slug = slugify(self.id)
            super(Serie, self).save(*args, **kwargs)

    def __str__(self):
        return self.titulo
    
class Temporada(models.Model):
    temporada = models.IntegerField()   
    serie = models.ForeignKey(Serie, on_delete=models.DO_NOTHING) 

    slug = models.SlugField()
    dt_cadastro = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
            self.slug = slugify(self.id)
            super(Temporada, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.temporada) + 'ª Temporada'
    
class Episodio(models.Model):
    numero = models.IntegerField()   
    nome = models.CharField(max_length=200)
    video = models.FileField(upload_to='videos') 
    serie = models.ForeignKey(Serie, on_delete=models.DO_NOTHING) 
    temporada = models.ForeignKey(Temporada, on_delete=models.DO_NOTHING) 

    slug = models.SlugField()
    dt_cadastro = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
            self.slug = slugify(self.id)
            super(Episodio, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.numero) + ': ' + str(self.nome)