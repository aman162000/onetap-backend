# Generated by Django 4.2.4 on 2023-09-18 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('beacon', '0001_initial'),
        ('attendance', '0002_alter_attendance_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='beacon',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='beacon.beacon'),
            preserve_default=False,
        ),
    ]