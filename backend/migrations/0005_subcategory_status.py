# Generated by Django 5.0 on 2024-04-03 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_delete_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='subcategory',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]