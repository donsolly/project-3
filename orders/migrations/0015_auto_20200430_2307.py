# Generated by Django 2.0.3 on 2020-04-30 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20200430_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='size',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
