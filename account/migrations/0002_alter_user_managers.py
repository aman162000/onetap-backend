# Generated by Django 4.2.4 on 2023-08-05 05:11

import account.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', account.models.CustomUserManager()),
            ],
        ),
    ]
