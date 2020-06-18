# -*- coding: utf-8 -*-
# Generated by Django 1.11.26 on 2019-12-18 14:43


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_metadata', '0227_bulkmodifyprogramhook'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalorganization',
            name='certificate_name',
            field=models.CharField(help_text='If populated, this field will overwrite name in platform.', max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='certificate_name',
            field=models.CharField(help_text='If populated, this field will overwrite name in platform.', max_length=255, null=True),
        ),
    ]
