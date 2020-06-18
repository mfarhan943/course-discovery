# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-11-20 17:49


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0220_leveltype_remove_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalseat',
            name='upgrade_deadline_override',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='seat',
            name='upgrade_deadline_override',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
