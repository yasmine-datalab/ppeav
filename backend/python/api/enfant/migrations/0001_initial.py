# Generated by Django 4.2 on 2023-04-08 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enfant',
            fields=[
                ('matricule', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
                ('sexe', models.CharField(max_length=50)),
                ('age', models.CharField(max_length=50)),
                ('vulnerabilite', models.CharField(max_length=50)),
            ],
            options={
                'ordering': ['nom'],
            },
        ),
    ]