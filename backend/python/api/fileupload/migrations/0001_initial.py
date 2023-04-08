# Generated by Django 4.2 on 2023-04-08 09:11

from django.db import migrations, models
import fileupload.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CSVFiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(choices=[('ENFANT', 'ENFANT'), ('STRUCTURE', 'STRUCTURE'), ('POINT DE RENCONTRE', 'POINT DE RENCONTRE')], max_length=20)),
                ('file', models.FileField(upload_to='<django.db.models.fields.CharField>_files', validators=[fileupload.models.validate_file], verbose_name='csv File')),
            ],
            options={
                'ordering': ['file'],
            },
        ),
    ]
