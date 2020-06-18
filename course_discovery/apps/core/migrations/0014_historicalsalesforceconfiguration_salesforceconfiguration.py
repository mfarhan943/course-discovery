# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-06-14 13:46


from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_historicalpartner'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalSalesforceConfiguration',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('username', models.CharField(max_length=255, verbose_name='Salesforce Username')),
                ('password', models.CharField(max_length=255, verbose_name='Salesforce Password')),
                ('organization_id', models.CharField(blank=True, default='', max_length=255, verbose_name='Salesforce Organization Id')),
                ('security_token', models.CharField(blank=True, default='', max_length=255, verbose_name='Salesforce Security Token')),
                ('is_sandbox', models.BooleanField(default=True, verbose_name='Is a Salesforce Sandbox?')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('partner', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='core.Partner')),
            ],
            options={
                'verbose_name': 'historical salesforce configuration',
                'get_latest_by': 'history_date',
                'ordering': ('-history_date', '-history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='SalesforceConfiguration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=255, verbose_name='Salesforce Username')),
                ('password', models.CharField(max_length=255, verbose_name='Salesforce Password')),
                ('organization_id', models.CharField(blank=True, default='', max_length=255, verbose_name='Salesforce Organization Id')),
                ('security_token', models.CharField(blank=True, default='', max_length=255, verbose_name='Salesforce Security Token')),
                ('is_sandbox', models.BooleanField(default=True, verbose_name='Is a Salesforce Sandbox?')),
                ('partner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='salesforce', to='core.Partner')),
            ],
        ),
    ]
