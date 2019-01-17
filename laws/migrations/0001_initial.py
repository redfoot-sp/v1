# Generated by Django 2.1.5 on 2019-01-07 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LawFile',
            fields=[
                ('type_law', models.CharField(choices=[('Decreto', 'Decreto'), ('Complementar', 'Lei Complementar'), ('Ordinaria', 'Lei Ordinária'), ('Organica', 'Lei Orgânica')], default='Decreto', max_length=16, verbose_name='Tipo')),
                ('id_law', models.AutoField(primary_key=True, serialize=False)),
                ('number_law', models.PositiveIntegerField(verbose_name='Número')),
                ('date_publish', models.DateField(verbose_name='Data da Publicação')),
                ('name_law', models.CharField(max_length=300, verbose_name='Nome/Descrição')),
                ('desc_law', models.TextField(verbose_name='Transcrição')),
                ('file_law', models.BinaryField(verbose_name='Arquivo')),
            ],
            options={
                'verbose_name_plural': 'Leis',
                'ordering': ('-date_publish',),
            },
        ),
    ]
