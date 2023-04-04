# Generated by Django 4.1.7 on 2023-04-02 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('description', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=200)),
                ('teacher', models.CharField(max_length=40)),
                ('time_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]