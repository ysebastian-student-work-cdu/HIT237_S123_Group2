# Generated by Django 4.1.7 on 2023-05-29 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('audit', '0005_alter_donate_date_alter_organisation_orgid_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donate',
            name='date',
        ),
    ]
