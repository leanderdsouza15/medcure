# Generated by Django 4.2.9 on 2024-03-04 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchS', '0006_remove_hospital_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='address',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='hospital',
            name='phone',
            field=models.CharField(default='', max_length=10),
        ),
    ]
