# Generated by Django 3.0.3 on 2020-09-07 10:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instrument', '0024_auto_20200907_1044'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='proventofii',
            unique_together={('instrument', 'ex_date', 'category', 'payment_date', 'value', 'reference_date')},
        ),
    ]