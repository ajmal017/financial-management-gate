# Generated by Django 3.0.3 on 2020-07-04 05:47

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instrument', '0013_remove_company_display'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='data',
            field=django.contrib.postgres.fields.jsonb.JSONField(default={}),
        ),
    ]