# Generated by Django 2.1.5 on 2020-06-10 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20200610_0844'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
            preserve_default=False,
        ),
    ]
