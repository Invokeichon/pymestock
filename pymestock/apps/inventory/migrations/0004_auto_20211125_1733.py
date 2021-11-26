# Generated by Django 3.2.5 on 2021-11-25 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0003_auto_20211125_1658'),
        ('inventory', '0003_remove_item_id_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='id_business',
        ),
        migrations.AddField(
            model_name='item',
            name='business',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='business.business'),
        ),
    ]