# Generated by Django 3.2.2 on 2021-05-10 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0009_rename_disc_directory_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='extension',
            field=models.CharField(default='none', max_length=4),
        ),
    ]
