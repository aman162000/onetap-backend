# Generated by Django 4.2.4 on 2023-10-11 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_student_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='subject',
            name='total_lecture',
            field=models.IntegerField(default=0, verbose_name='Total lectures'),
        ),
    ]
