# Generated by Django 4.2.1 on 2023-05-30 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfoliopost',
            name='description',
            field=models.TextField(default='Default description'),
        ),
    ]
