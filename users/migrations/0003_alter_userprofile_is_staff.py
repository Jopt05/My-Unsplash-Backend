# Generated by Django 4.0.4 on 2023-07-24 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_userprofile_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
    ]