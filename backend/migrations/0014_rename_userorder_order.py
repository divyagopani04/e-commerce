# Generated by Django 4.2.5 on 2024-05-28 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_userorder'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='userorder',
            new_name='order',
        ),
    ]
