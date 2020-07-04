# Generated by Django 3.0.3 on 2020-07-04 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instrument', '0014_auto_20200704_0547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrument',
            name='cFICd',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='cFICd'),
        ),
        migrations.AlterField(
            model_name='instrument',
            name='corpGovnLvlNm',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='corpGovnLvlNm'),
        ),
        migrations.AlterField(
            model_name='instrument',
            name='crpnNm',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='crpnNm'),
        ),
        migrations.AlterField(
            model_name='instrument',
            name='isin',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='isin'),
        ),
        migrations.AlterField(
            model_name='instrument',
            name='mktNm',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='mktNm'),
        ),
        migrations.AlterField(
            model_name='instrument',
            name='sctyCtgyNm',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='SctyCtgyNm'),
        ),
        migrations.AlterField(
            model_name='instrument',
            name='sgmtNm',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='sgmtNm'),
        ),
    ]
