# Generated by Django 3.0.3 on 2020-07-11 20:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instrument', '0017_auto_20200711_2025'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='split',
            unique_together={('instrument', 'ex_date', 'category', 'event_date', 'factor', 'income_tax_price', 'fraction_price', 'fraction_date')},
        ),
    ]