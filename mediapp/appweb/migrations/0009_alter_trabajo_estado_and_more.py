# Generated by Django 4.2.1 on 2023-07-11 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appweb', '0008_mecanico_correo_mecanico_passwd_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajo',
            name='estado',
            field=models.CharField(default='P', max_length=1),
        ),
        migrations.AlterField(
            model_name='trabajo',
            name='motivo_desaprobacion',
            field=models.CharField(default='none', max_length=250),
        ),
    ]