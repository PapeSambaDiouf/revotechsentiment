# Generated by Django 5.0.2 on 2024-03-04 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produit',
            name='status',
        ),
    ]
