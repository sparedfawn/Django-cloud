# Generated by Django 3.2.2 on 2021-05-27 13:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0010_file_extension'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publiclink',
            name='URL',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='publiclink',
            name='generationDate',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
