# Generated by Django 3.2 on 2021-04-07 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publiclink',
            old_name='expireDate',
            new_name='generationDate',
        ),
        migrations.RemoveField(
            model_name='directory',
            name='accessPath',
        ),
        migrations.RemoveField(
            model_name='file',
            name='binID',
        ),
        migrations.AddField(
            model_name='file',
            name='inBin',
            field=models.BooleanField(default=False),
        ),
    ]