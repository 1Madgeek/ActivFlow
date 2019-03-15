# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('module_ref', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Initiated', 'Initiated'), ('Withdrawn', 'Withdrawn'), ('Completed', 'Completed')], max_length=30, verbose_name='Status')),
                ('requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date')),
                ('last_updated', models.DateTimeField(auto_now=True, verbose_name='Last Updated')),
                ('activity_ref', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('Not Started', 'Not Started'), ('In Progress', 'In Progress'), ('Rolled Back', 'Rolled Back'), ('Completed', 'Completed')], max_length=30, verbose_name='Status')),
                ('assignee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='core.Request')),
                ('updated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
