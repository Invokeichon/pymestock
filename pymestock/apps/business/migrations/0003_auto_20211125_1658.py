# Generated by Django 3.2.5 on 2021-11-25 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0002_auto_20211124_2156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='owner',
        ),
        migrations.AlterField(
            model_name='business',
            name='business_name',
            field=models.CharField(max_length=100),
        ),
    ]
