# Generated by Django 4.2.4 on 2023-10-18 04:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_subject_total_lecture'),
        ('attendance', '0007_alter_attendance_beacon'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='taken_by',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='account.teacher'),
            preserve_default=False,
        ),
    ]
