# Generated by Django 3.0.3 on 2020-07-10 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instrument', '0016_auto_20200710_0445'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dividend',
            old_name='dividends_type',
            new_name='dividend_type',
        ),
    ]