# Generated by Django 3.1.4 on 2021-01-04 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20210103_2348'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='genre_fk',
            new_name='genre',
        ),
    ]
