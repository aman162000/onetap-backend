# Generated by Django 4.2.4 on 2023-09-29 04:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_attendance_beacon'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='attendance',
            unique_together=set(),
        ),
    ]
