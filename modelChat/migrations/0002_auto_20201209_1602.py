# Generated by Django 3.0.8 on 2020-12-09 10:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modelChat', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='file',
            old_name='image',
            new_name='file',
        ),
    ]
