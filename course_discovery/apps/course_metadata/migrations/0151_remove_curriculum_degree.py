# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-02-04 17:04


from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0150_curriculum_program'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='curriculum',
            name='degree',
        ),
    ]
