# Generated by Django 3.2.5 on 2021-11-25 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20211125_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='sku',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
