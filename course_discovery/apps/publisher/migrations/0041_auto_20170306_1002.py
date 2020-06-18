# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-06 10:02


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('publisher', '0040_auto_20170223_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courserunstate',
            name='approved_by_role',
            field=models.CharField(blank=True, choices=[('partner_manager', 'Partner Manager'), ('project_coordinator', 'Project Coordinator'), ('marketing_reviewer', 'Marketing Reviewer'), ('publisher', 'Publisher'), ('course_team', 'Course Team')], max_length=63, null=True),
        ),
        migrations.AlterField(
            model_name='courserunstate',
            name='owner_role',
            field=models.CharField(choices=[('partner_manager', 'Partner Manager'), ('project_coordinator', 'Project Coordinator'), ('marketing_reviewer', 'Marketing Reviewer'), ('publisher', 'Publisher'), ('course_team', 'Course Team')], max_length=63),
        ),
        migrations.AlterField(
            model_name='coursestate',
            name='approved_by_role',
            field=models.CharField(blank=True, choices=[('partner_manager', 'Partner Manager'), ('project_coordinator', 'Project Coordinator'), ('marketing_reviewer', 'Marketing Reviewer'), ('publisher', 'Publisher'), ('course_team', 'Course Team')], max_length=63, null=True),
        ),
        migrations.AlterField(
            model_name='coursestate',
            name='owner_role',
            field=models.CharField(choices=[('partner_manager', 'Partner Manager'), ('project_coordinator', 'Project Coordinator'), ('marketing_reviewer', 'Marketing Reviewer'), ('publisher', 'Publisher'), ('course_team', 'Course Team')], max_length=63),
        ),
        migrations.AlterField(
            model_name='courseuserrole',
            name='role',
            field=models.CharField(choices=[('partner_manager', 'Partner Manager'), ('project_coordinator', 'Project Coordinator'), ('marketing_reviewer', 'Marketing Reviewer'), ('publisher', 'Publisher'), ('course_team', 'Course Team')], max_length=63, verbose_name='Course Role'),
        ),
        migrations.AlterField(
            model_name='historicalcourserunstate',
            name='approved_by_role',
            field=models.CharField(blank=True, choices=[('partner_manager', 'Partner Manager'), ('project_coordinator', 'Project Coordinator'), ('marketing_reviewer', 'Marketing Reviewer'), ('publisher', 'Publisher'), ('course_team', 'Course Team')], max_length=63, null=True),
        ),
        migrations.AlterField(
            model_name='historicalcourserunstate',
            name='owner_role',
            field=models.CharField(choices=[('partner_manager', 'Partner Manager'), ('project_coordinator', 'Project Coordinator'), ('marketing_reviewer', 'Marketing Reviewer'), ('publisher', 'Publisher'), ('course_team', 'Course Team')], max_length=63),
        ),
        migrations.AlterField(
            model_name='historicalcoursestate',
            name='approved_by_role',
            field=models.CharField(blank=True, choices=[('partner_manager', 'Partner Manager'), ('project_coordinator', 'Project Coordinator'), ('marketing_reviewer', 'Marketing Reviewer'), ('publisher', 'Publisher'), ('course_team', 'Course Team')], max_length=63, null=True),
        ),
        migrations.AlterField(
            model_name='historicalcoursestate',
            name='owner_role',
            field=models.CharField(choices=[('partner_manager', 'Partner Manager'), ('project_coordinator', 'Project Coordinator'), ('marketing_reviewer', 'Marketing Reviewer'), ('publisher', 'Publisher'), ('course_team', 'Course Team')], max_length=63),
        ),
        migrations.AlterField(
            model_name='historicalcourseuserrole',
            name='role',
            field=models.CharField(choices=[('partner_manager', 'Partner Manager'), ('project_coordinator', 'Project Coordinator'), ('marketing_reviewer', 'Marketing Reviewer'), ('publisher', 'Publisher'), ('course_team', 'Course Team')], max_length=63, verbose_name='Course Role'),
        ),
        migrations.AlterField(
            model_name='historicalorganizationuserrole',
            name='role',
            field=models.CharField(choices=[('partner_manager', 'Partner Manager'), ('project_coordinator', 'Project Coordinator'), ('marketing_reviewer', 'Marketing Reviewer'), ('publisher', 'Publisher'), ('course_team', 'Course Team')], max_length=63, verbose_name='Organization Role'),
        ),
        migrations.AlterField(
            model_name='organizationuserrole',
            name='role',
            field=models.CharField(choices=[('partner_manager', 'Partner Manager'), ('project_coordinator', 'Project Coordinator'), ('marketing_reviewer', 'Marketing Reviewer'), ('publisher', 'Publisher'), ('course_team', 'Course Team')], max_length=63, verbose_name='Organization Role'),
        ),
    ]
