# Generated by Django 5.0 on 2024-05-21 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_contactinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='billing_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bcountry', models.CharField(max_length=100)),
                ('bfirstname', models.CharField(max_length=100)),
                ('blastname', models.CharField(max_length=100)),
                ('bcompanyname', models.CharField(max_length=100)),
                ('baddress', models.CharField(max_length=100)),
                ('bcity', models.CharField(max_length=100)),
                ('bstate', models.CharField(max_length=100)),
                ('bzipcode', models.CharField(max_length=100)),
                ('bemail', models.EmailField(max_length=100)),
                ('bphone', models.CharField(max_length=100)),
                ('bmessage', models.CharField(max_length=100)),
            ],
        ),
    ]