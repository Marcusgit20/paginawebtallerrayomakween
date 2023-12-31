# Generated by Django 4.2.1 on 2023-06-23 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('telefono', models.IntegerField()),
                ('tipo_contacto', models.IntegerField(choices=[[0, 'Sugerencia'], [1, 'Reclamo'], [2, 'Felicitaciones']])),
                ('mensaje', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Mecanico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rut', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=80)),
                ('apellido', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
                ('fecha_nacimiento', models.DateField()),
                ('test', models.CharField(max_length=10)),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appweb.cargo')),
            ],
        ),
    ]
