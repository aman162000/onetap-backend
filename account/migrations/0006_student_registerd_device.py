# Generated by Django 4.2.4 on 2023-09-26 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_user_created_at_user_onboarding_completed_user_uid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='registerd_device',
            field=models.CharField(default='', max_length=255),
        ),
    ]
