# Generated by Django 4.2.9 on 2024-03-01 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('searchS', '0003_alter_hospital_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospital',
            name='map_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]