# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-04-22 14:01


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0169_rename_official_version'),
    ]

    operations = [
        migrations.AddField(
            model_name='courserun',
            name='go_live_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
