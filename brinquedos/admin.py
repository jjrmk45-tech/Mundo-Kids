from django.contrib import admin
from .models import Brinquedo


@admin.register(Brinquedo)
class BrinquedoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'preco', 'estoque', 'faixa_etaria')
    list_filter = ('categoria',)
    search_fields = ('nome', 'descricao')
    fields = (
        'nome',
        'descricao',
        'categoria',
        'imagem',
        'preco',
        'estoque',
        'faixa_etaria',
    )