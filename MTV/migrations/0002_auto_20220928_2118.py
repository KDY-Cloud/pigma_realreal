# Generated by Django 3.1 on 2022-09-28 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MTV', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]