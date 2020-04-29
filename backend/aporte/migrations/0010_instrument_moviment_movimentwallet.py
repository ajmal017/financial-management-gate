# Generated by Django 3.0.3 on 2020-04-29 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
        ('aporte', '0009_delete_selic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instrument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tckrSymb', models.CharField(max_length=20, unique=True, verbose_name='tckrSymb')),
                ('crpn', models.CharField(blank=True, max_length=20, null=True, verbose_name='crpnNm')),
                ('sgmtNm', models.CharField(blank=True, max_length=20, null=True, verbose_name='sgmtNm')),
                ('mktNm', models.CharField(max_length=20, verbose_name='mktNm')),
                ('mctyCtgyNm', models.CharField(blank=True, max_length=20, null=True, verbose_name='mctyCtgyNm')),
                ('isin', models.CharField(blank=True, max_length=20, null=True, verbose_name='isin')),
                ('corpGovnLvlNm', models.CharField(blank=True, max_length=20, null=True, verbose_name='corpGovnLvlNm')),
                ('cFICd', models.CharField(blank=True, max_length=20, null=True, verbose_name='cFICd')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
            ],
            options={
                'verbose_name': 'Instrument',
                'verbose_name_plural': 'Instruments',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Moviment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(0, 'COMPRA'), (1, 'VENDA')], verbose_name='type')),
                ('quantity', models.IntegerField(verbose_name='quantity')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='price')),
                ('costs', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='costs')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('instrument', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aporte.Instrument')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MovimentWallet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('moviment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aporte.Moviment')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wallet.Wallet')),
            ],
            options={
                'verbose_name': 'Moviments Wallet',
                'verbose_name_plural': 'Moviments Wallets',
            },
        ),
    ]
