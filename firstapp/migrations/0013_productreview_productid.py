# Generated by Django 5.0 on 2024-05-09 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0012_productreview'),
    ]

    operations = [
        migrations.AddField(
            model_name='productreview',
            name='productid',
            field=models.IntegerField(default=0),
        ),
    ]
