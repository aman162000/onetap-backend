# Generated by Django 4.2.4 on 2023-08-06 07:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_user_managers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]