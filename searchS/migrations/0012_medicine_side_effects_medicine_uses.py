# Generated by Django 4.2.9 on 2024-03-10 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchS', '0011_alter_medicine_cost_alter_medicine_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicine',
            name='side_effects',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='medicine',
            name='uses',
            field=models.TextField(blank=True),
        ),
    ]