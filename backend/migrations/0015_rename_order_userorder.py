# Generated by Django 4.2.5 on 2024-06-01 07:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_rename_userorder_order'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='order',
            new_name='userorder',
        ),
    ]