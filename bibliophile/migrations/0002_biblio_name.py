# Generated by Django 3.0.8 on 2020-07-31 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliophile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='biblio',
            name='name',
            field=models.CharField(default='something', max_length=100),
        ),
    ]