# Generated by Django 3.0.14 on 2021-10-31 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TradingRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avg_price', models.FloatField()),
                ('executed_qty', models.FloatField()),
                ('fee', models.FloatField()),
                ('cum_quote', models.FloatField()),
                ('side', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=20)),
                ('type', models.CharField(max_length=20)),
                ('symbol', models.CharField(max_length=20)),
                ('trade_diff_rate', models.FloatField()),
                ('target_price', models.FloatField()),
                ('datetime', models.DateTimeField()),
            ],
        ),
    ]