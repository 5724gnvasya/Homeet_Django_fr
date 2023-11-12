# Generated by Django 4.2.7 on 2023-11-12 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('users_photo', models.ImageField(upload_to=None)),
                ('first_name', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField(max_length=30)),
                ('telegram', models.CharField(max_length=30)),
                ('nom_tel', models.CharField(max_length=30)),
                ('osebe', models.CharField(max_length=30)),
                ('student', models.CharField(max_length=30)),
                ('curs', models.CharField(max_length=30)),
                ('stupen_obrazov', models.CharField(max_length=30)),
                ('facultet', models.CharField(max_length=30)),
                ('obrazov_pr', models.CharField(max_length=30)),
                ('rabota', models.CharField(max_length=30)),
            ],
        ),
    ]