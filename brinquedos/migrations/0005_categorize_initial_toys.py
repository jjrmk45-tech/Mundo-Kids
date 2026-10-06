from django.db import migrations


TOY_PRESENTATION = {
    'Carrinho de Controle Remoto': {
        'categoria': 'meninos',
        'imagem': 'carro-controle-remoto.png',
    },
    'Urso de Pelúcia': {
        'categoria': 'bebes',
    },
    'Bola Colorida': {
        'categoria': 'ao_ar_livre',
    },
    'Boneca Fashion': {
        'categoria': 'meninas',
    },
    'Blocos de Montar': {
        'categoria': 'educacao',
        'imagem': 'brinquedo-de-empilhar.png',
    },
    'Jogo de Tabuleiro': {
        'categoria': 'jogos',
        'imagem': 'genius.png',
    },
    'Avião de Brinquedo': {
        'categoria': 'ao_ar_livre',
    },
    'Robô Educativo': {
        'categoria': 'criativos',
        'imagem': 'robo-roxo.png',
    },
}


def categorize_initial_toys(apps, schema_editor):
    brinquedo_model = apps.get_model('brinquedos', 'Brinquedo')
    database = schema_editor.connection.alias

    for nome, presentation in TOY_PRESENTATION.items():
        brinquedo_model.objects.using(database).filter(nome=nome).update(
            **presentation
        )


class Migration(migrations.Migration):

    dependencies = [
        ('brinquedos', '0004_brinquedo_categoria_brinquedo_imagem'),
    ]

    operations = [
        migrations.RunPython(categorize_initial_toys, migrations.RunPython.noop),
    ]
