# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-12-12 20:16
from __future__ import unicode_literals

import stdimage.models
from django.db import migrations, models

import course_discovery.apps.course_metadata.utils
import course_discovery.apps.publisher.validators


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0061_add_people_permission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=stdimage.models.StdImageField(blank=True, null=True, upload_to=course_discovery.apps.course_metadata.utils.UploadToFieldNamePath('number', path='media/publisher/courses/images'), validators=[course_discovery.apps.publisher.validators.ImageMultiSizeValidator([(2120, 1192), (1134, 675), (378, 225)])]),
        ),
        migrations.AlterField(
            model_name='historicalcourse',
            name='image',
            field=models.TextField(blank=True, max_length=100, null=True, validators=[course_discovery.apps.publisher.validators.ImageMultiSizeValidator([(2120, 1192), (1134, 675), (378, 225)])]),
        ),
    ]
