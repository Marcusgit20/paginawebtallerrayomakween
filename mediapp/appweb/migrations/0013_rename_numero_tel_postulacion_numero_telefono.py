# Generated by Django 4.2.1 on 2023-07-14 01:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0012_remove_postulacion_id_postulacion_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='postulacion',
            old_name='numero_tel',
            new_name='numero_telefono',
        ),
    ]
