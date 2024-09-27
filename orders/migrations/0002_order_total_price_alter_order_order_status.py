# Generated by Django 5.1.1 on 2024-09-27 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.IntegerField(choices=[(2, 'ORDER_PROSSED'), (3, 'ORDER_DELEVERED'), (4, 'ORDER_REJECTED'), (1, 'ORDER_CONFORMED')], default=0),
        ),
    ]
