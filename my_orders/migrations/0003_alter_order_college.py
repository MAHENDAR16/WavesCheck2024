# Generated by Django 4.0.6 on 2024-01-31 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_orders', '0002_remove_order_referral_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='college',
            field=models.CharField(max_length=150),
        ),
    ]
