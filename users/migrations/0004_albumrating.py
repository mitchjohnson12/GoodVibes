# Generated by Django 3.1.4 on 2021-02-07 03:00

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_auto_20210103_2349'),
        ('users', '0003_auto_20210112_2303'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlbumRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('star_review', models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('date_first_added', models.DateTimeField(auto_now_add=True)),
                ('private_notes', models.TextField(max_length=1000)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.album')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
        ),
    ]
