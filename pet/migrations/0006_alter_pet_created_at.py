# Generated by Django 5.0.1 on 2024-01-16 19:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0005_alter_pet_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='created_at',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
