# Generated by Django 3.2 on 2021-04-07 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Directory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('directoryName', models.CharField(max_length=20)),
                ('accessPath', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fileName', models.CharField(max_length=30)),
                ('uploadDate', models.DateTimeField()),
                ('binID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.bin')),
                ('directoryID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.directory')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PublicLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('URL', models.URLField(max_length=50)),
                ('expireDate', models.DateTimeField()),
                ('fileID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.file')),
            ],
        ),
        migrations.CreateModel(
            name='PrivateDisc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discName', models.CharField(max_length=20)),
                ('binID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.bin')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.user')),
            ],
        ),
        migrations.AddField(
            model_name='directory',
            name='discID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.privatedisc'),
        ),
    ]