from django.db import migrations


def clear_mismatched_product_image(apps, schema_editor):
    brinquedo_model = apps.get_model('brinquedos', 'Brinquedo')
    brinquedo_model.objects.using(schema_editor.connection.alias).filter(
        nome='Blocos de Montar',
    ).update(imagem='')


class Migration(migrations.Migration):

    dependencies = [
        ('brinquedos', '0005_categorize_initial_toys'),
    ]

    operations = [
        migrations.RunPython(
            clear_mismatched_product_image,
            migrations.RunPython.noop,
        ),
    ]
