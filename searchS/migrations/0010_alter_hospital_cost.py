# Generated by Django 4.2.9 on 2024-03-07 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchS', '0009_remove_medicine_name_remove_medicine_stores_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]