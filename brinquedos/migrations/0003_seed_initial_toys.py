from django.db import migrations


INITIAL_TOYS = [
    {
        'nome': 'Carrinho de Controle Remoto',
        'preco': '129.90',
        'estoque': 15,
        'faixa_etaria': 'A partir de 6 anos',
    },
    {
        'nome': 'Urso de Pelúcia',
        'preco': '59.90',
        'estoque': 20,
        'faixa_etaria': 'A partir de 3 anos',
    },
    {
        'nome': 'Bola Colorida',
        'preco': '29.90',
        'estoque': 30,
        'faixa_etaria': 'A partir de 3 anos',
    },
    {
        'nome': 'Boneca Fashion',
        'preco': '79.90',
        'estoque': 12,
        'faixa_etaria': 'A partir de 5 anos',
    },
    {
        'nome': 'Blocos de Montar',
        'preco': '89.90',
        'estoque': 18,
        'faixa_etaria': 'A partir de 5 anos',
    },
    {
        'nome': 'Jogo de Tabuleiro',
        'preco': '69.90',
        'estoque': 10,
        'faixa_etaria': 'A partir de 8 anos',
    },
    {
        'nome': 'Avião de Brinquedo',
        'preco': '45.90',
        'estoque': 14,
        'faixa_etaria': 'A partir de 4 anos',
    },
    {
        'nome': 'Robô Educativo',
        'preco': '149.90',
        'estoque': 8,
        'faixa_etaria': 'A partir de 7 anos',
    },
]


def add_initial_toys(apps, schema_editor):
    brinquedo_model = apps.get_model('brinquedos', 'Brinquedo')
    database = schema_editor.connection.alias

    for toy in INITIAL_TOYS:
        brinquedo_model.objects.using(database).get_or_create(
            nome=toy['nome'],
            defaults=toy,
        )


class Migration(migrations.Migration):

    dependencies = [
        ('brinquedos', '0002_brinquedo_faixa_etaria_alter_brinquedo_descricao'),
    ]

    operations = [
        migrations.RunPython(add_initial_toys, migrations.RunPython.noop),
    ]
