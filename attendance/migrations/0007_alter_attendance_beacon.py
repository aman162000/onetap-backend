# Generated by Django 4.2.4 on 2023-09-29 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0006_alter_attendance_beacon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='beacon',
            field=models.CharField(max_length=255),
        ),
    ]
