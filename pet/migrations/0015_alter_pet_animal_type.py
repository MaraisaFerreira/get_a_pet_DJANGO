# Generated by Django 5.0.1 on 2024-01-29 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0014_alter_userprofile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='animal_type',
            field=models.CharField(choices=[('cat', 'Gato'), ('dog', 'Cachorro'), ('hamster', 'Hamster'), ('rabbit', 'Coelho')], default='cat', max_length=8),
        ),
    ]
