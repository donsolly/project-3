# Generated by Django 2.0.3 on 2020-04-30 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0011_auto_20200430_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='price',
            field=models.CharField(max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True),
        ),
    ]
