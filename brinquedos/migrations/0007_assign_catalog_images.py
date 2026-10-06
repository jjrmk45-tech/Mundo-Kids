from django.db import migrations


IMAGE_BY_TOY = {
    'Carrinho de Controle Remoto': 'carro-controle-remoto.png',
    'Urso de Pelúcia': 'brinquedo-bebe-aneis.png',
    'Bola Colorida': 'brinquedo-mercado.png',
    'Boneca Fashion': 'brinquedo-bonecas.png',
    'Blocos de Montar': 'brinquedo-de-empilhar.png',
    'Jogo de Tabuleiro': 'brinquedo-uno.png',
    'Avião de Brinquedo': 'brinquedo-skate.png',
    'Robô Educativo': 'brinquedo-caderno.png',
}


def assign_catalog_images(apps, schema_editor):
    brinquedo_model = apps.get_model('brinquedos', 'Brinquedo')
    database = schema_editor.connection.alias

    for nome, imagem in IMAGE_BY_TOY.items():
        brinquedo_model.objects.using(database).filter(nome=nome).update(imagem=imagem)


class Migration(migrations.Migration):

    dependencies = [
        ('brinquedos', '0006_clear_mismatched_product_image'),
    ]

    operations = [
        migrations.RunPython(assign_catalog_images, migrations.RunPython.noop),
    ]
