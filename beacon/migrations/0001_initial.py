# Generated by Django 4.2.4 on 2023-09-18 17:22

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0004_teacher_subject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beacon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('minor_value', models.IntegerField(help_text='The unique identifier for the subject associated with this beacon.', verbose_name='Subject Id')),
                ('lecturer', models.ForeignKey(help_text='The lecturer associated with this beacon.', on_delete=django.db.models.deletion.CASCADE, to='account.teacher')),
                ('subject', models.ForeignKey(help_text='The subject associated with this beacon.', on_delete=django.db.models.deletion.CASCADE, to='account.subject')),
            ],
            options={
                'verbose_name': 'Beacon',
                'verbose_name_plural': 'Beacons',
            },
        ),
    ]
