# Generated by Django 4.1.7 on 2023-05-31 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0011_alter_donate_amount_alter_donate_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.AlterField(
            model_name='donate',
            name='amount',
            field=models.IntegerField(verbose_name='Amount(kg)'),
        ),
    ]
