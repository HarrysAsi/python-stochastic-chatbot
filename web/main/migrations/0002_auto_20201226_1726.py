# Generated by Django 3.1.4 on 2020-12-26 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='tag',
            new_name='tags',
        ),
    ]
