# Generated by Django 2.1.5 on 2020-06-07 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200606_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dinnerplatters',
            name='upsize',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='pizza',
            name='upsize',
            field=models.CharField(max_length=4),
        ),
        migrations.AlterField(
            model_name='sub',
            name='upsize',
            field=models.CharField(max_length=4),
        ),
    ]
