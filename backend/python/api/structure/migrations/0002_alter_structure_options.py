# Generated by Django 4.1.7 on 2023-04-01 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='structure',
            options={'ordering': ['structure']},
        ),
    ]