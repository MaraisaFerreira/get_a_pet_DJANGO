# Generated by Django 5.0.1 on 2024-01-16 15:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0002_pet_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pet',
            name='size',
        ),
        migrations.AlterField(
            model_name='pet',
            name='age_type',
            field=models.CharField(choices=[('dias', 'Dias'), ('meses', 'Meses'), ('anos', 'Anos')], default='dias', max_length=5),
        ),
        migrations.AlterField(
            model_name='pet',
            name='available',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='pet',
            name='color',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='pet',
            name='created_at',
            field=models.DateField(default=datetime.datetime(2024, 1, 16, 15, 57, 40, 870887, tzinfo=datetime.timezone.utc)),
        ),
    ]