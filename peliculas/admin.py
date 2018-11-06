from django.contrib import admin
from django.contrib import admin
from peliculas.models import Actor, ActorAdmin, Pelicula, PeliculaAdmin

# Register your models here.
admin.site.register(Actor, ActorAdmin)
admin.site.register(Pelicula, PeliculaAdmin)
