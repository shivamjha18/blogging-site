# Generated by Django 3.0.6 on 2021-04-15 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='number',
            new_name='phone',
        ),
    ]
