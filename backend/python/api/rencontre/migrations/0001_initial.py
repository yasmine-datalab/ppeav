# Generated by Django 4.2 on 2023-04-08 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rencontre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codecoupon', models.CharField(max_length=100)),
                ('ville', models.CharField(max_length=100)),
                ('lieu', models.CharField(max_length=100)),
                ('longitude', models.DecimalField(decimal_places=10, max_digits=15)),
                ('latitude', models.DecimalField(decimal_places=10, max_digits=15)),
            ],
            options={
                'ordering': ['codecoupon'],
            },
        ),
    ]
