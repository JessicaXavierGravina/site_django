from django.contrib import admin
from .models import Filme, Episodio, Usuario
from django.contrib.auth.admin import UserAdmin

#aparecer filmes_vistos em um campo personalizado no admin do site, sem isso ele ainda teria o campo, porém, nao seria visto pelo admin
campos = list(UserAdmin.fieldsets)
campos.append(
    ('Histórico', {'fields': ('filmes_vistos',)})
)
UserAdmin.fieldsets = tuple(campos)

# Register your models here.
admin.site.register(Filme)
admin.site.register(Episodio)
admin.site.register(Usuario, UserAdmin)