# Generated by Django 4.2.5 on 2024-04-13 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0004_rename_fname_myprofile_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='myprofile',
            old_name='name',
            new_name='fname',
        ),
    ]
