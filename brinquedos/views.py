from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from .models import Brinquedo


CATEGORIA_ICONES = {
    Brinquedo.CATEGORIA_MENINOS: '🚗',
    Brinquedo.CATEGORIA_MENINAS: '🎀',
    Brinquedo.CATEGORIA_BEBES: '🧸',
    Brinquedo.CATEGORIA_EDUCACAO: '🧩',
    Brinquedo.CATEGORIA_JOGOS: '🎮',
    Brinquedo.CATEGORIA_AR_LIVRE: '⚽',
    Brinquedo.CATEGORIA_CRIATIVOS: '🎨',
}


def filtrar_brinquedos(request):
    query = request.GET.get('q', '').strip()
    categoria = request.GET.get('categoria', '').strip()
    categorias_validas = {valor for valor, _ in Brinquedo.CATEGORIAS}
    if categoria not in categorias_validas:
        categoria = ''

    brinquedos = Brinquedo.objects.all()
    if query:
        brinquedos = brinquedos.filter(
            Q(nome__icontains=query)
            | Q(descricao__icontains=query)
            | Q(faixa_etaria__icontains=query)
        )
    if categoria:
        brinquedos = brinquedos.filter(categoria=categoria)

    return brinquedos.order_by('nome'), query, categoria


def contexto_listagem(request, nome_url):
    brinquedos, query, categoria = filtrar_brinquedos(request)
    categorias = [
        {'valor': '', 'nome': 'Todos os produtos', 'icone': '▦'},
        *[
            {'valor': valor, 'nome': nome, 'icone': CATEGORIA_ICONES[valor]}
            for valor, nome in Brinquedo.CATEGORIAS
        ],
    ]
    nome_categoria = dict(Brinquedo.CATEGORIAS).get(categoria, '')
    return {
        'brinquedos': brinquedos,
        'query': query,
        'categoria_selecionada': categoria,
        'nome_categoria': nome_categoria,
        'categorias': categorias,
        'url_listagem': nome_url,
    }


def index(request):
    return render(
        request,
        'brinquedos/index.html',
        contexto_listagem(request, 'index'),
    )


def catalogo(request):
    return render(
        request,
        'brinquedos/catalogo.html',
        contexto_listagem(request, 'catalogo'),
    )


def detalhe(request, id):
    brinquedo = get_object_or_404(Brinquedo, id=id)

    return render(
        request,
        'brinquedos/detalhe.html',
        {'brinquedo': brinquedo}
    )
