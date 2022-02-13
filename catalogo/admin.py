from django.contrib import admin

# Register your models here.

from catalogo.models import Genero, Linguagem, Autor, Livro, ExemplarLivro


# Registro para poder usar no painel admin do django
admin.site.register(Genero)
admin.site.register(Linguagem)
admin.site.register(Autor)
admin.site.register(Livro)
admin.site.register(ExemplarLivro)


