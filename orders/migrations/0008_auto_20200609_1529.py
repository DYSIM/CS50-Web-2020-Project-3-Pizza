# Generated by Django 2.1.5 on 2020-06-09 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20200609_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub_addition',
            name='Size',
            field=models.CharField(max_length=5, null=True),
        ),
    ]
