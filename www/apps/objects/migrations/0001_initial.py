# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-06 09:03
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import proj.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('activities', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locale', models.CharField(blank=True, db_index=True, max_length=2, null=True, verbose_name='локаль')),
                ('index', models.PositiveIntegerField(db_index=True, default=0, verbose_name='индекс')),
                ('robots', proj.db.fields.StripCharField(blank=True, choices=[(None, 'ALL'), ('index,nofollow', 'index, no follow'), ('noindex,noarchive,follow', 'no index, follow'), ('noindex,noarchive,nofollow', 'NONE')], max_length=32, null=True)),
                ('title', proj.db.fields.StripCharField(blank=True, max_length=255, null=True)),
                ('keywords', proj.db.fields.StripCharField(blank=True, max_length=255, null=True)),
                ('description', proj.db.fields.StripCharField(blank=True, max_length=255, null=True)),
                ('name', proj.db.fields.StripCharField(max_length=255, null=True, verbose_name='заголовок')),
                ('label', proj.db.fields.StripCharField(blank=True, max_length=80, null=True, verbose_name='пункт меню')),
                ('aliace', proj.db.fields.StripCharField(blank=True, max_length=1024, null=True)),
                ('slug', proj.db.fields.StripCharField(blank=True, db_index=True, max_length=1024, null=True, verbose_name='URI')),
                ('published', models.BooleanField(db_index=True, default=False, verbose_name='в публикации')),
                ('published_date', models.DateField(blank=True, db_index=True, null=True, verbose_name='старт')),
                ('archived', models.BooleanField(db_index=True, default=False, verbose_name='в архиве')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='создано')),
                ('change_date', models.DateTimeField(auto_now=True, verbose_name='изменено')),
                ('actual', models.BooleanField(db_index=True, default=False, verbose_name='в работе')),
                ('address', proj.db.fields.StripCharField(max_length=255, verbose_name='адрес')),
                ('longitude', models.FloatField(blank=True, default=0, verbose_name='долгота')),
                ('latitude', models.FloatField(blank=True, default=0, verbose_name='широта')),
                ('zoom', models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='зум')),
                ('customer', proj.db.fields.StripCharField(max_length=128, verbose_name='заказчик')),
                ('developer', proj.db.fields.StripCharField(blank=True, max_length=128, null=True, verbose_name='застройщик')),
                ('start_date', models.DateField(blank=True, null=True, verbose_name='начало работ')),
                ('finish_date', models.DateField(blank=True, null=True, verbose_name='окончание работ')),
                ('note', proj.db.fields.StripTextField(blank=True, null=True, verbose_name='примечания')),
                ('activity', models.ManyToManyField(blank=True, db_table='cck_object_activity', to='activities.Activity', verbose_name='деятельность')),
                ('change_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='редактор')),
                ('create_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='автор')),
            ],
            options={
                'verbose_name': 'объект',
                'verbose_name_plural': 'объекты',
                'ordering': ('-locale', '-actual', 'index'),
                'db_table': 'cck_object',
            },
        ),
        migrations.AlterUniqueTogether(
            name='object',
            unique_together=set([('locale', 'slug')]),
        ),
    ]
