# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-18 17:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import proj.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sites', '0002_alter_domain_unique'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', proj.db.fields.StripCharField(db_index=True, max_length=128, verbose_name='имя')),
                ('phone', proj.db.fields.StripCharField(db_index=True, max_length=128, verbose_name='телефон')),
                ('sent_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='дата')),
                ('state', models.NullBooleanField(db_index=True, verbose_name='обратный звонок')),
                ('note', proj.db.fields.StripTextField(blank=True, null=True, verbose_name='примечание')),
                ('agent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='агент')),
                ('site', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='sites.Site', verbose_name='сайт')),
            ],
            options={
                'db_table': 'proj_callback',
                'verbose_name_plural': 'заказы',
                'ordering': ('state', '-sent_date', 'site'),
                'verbose_name': 'заказ',
            },
        ),
    ]
