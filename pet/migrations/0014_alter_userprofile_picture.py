# Generated by Django 5.0.1 on 2024-01-26 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0013_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='user_imgs/%Y'),
        ),
    ]
