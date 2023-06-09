# Generated by Django 4.1.7 on 2023-05-29 01:22

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameofItem1', models.CharField(max_length=100)),
                ('quantity1', models.IntegerField()),
                ('nameofItem2', models.CharField(max_length=100)),
                ('quantity2', models.IntegerField()),
                ('nameofItem3', models.CharField(max_length=100)),
                ('quantity3', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('orgid', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True)),
                ('type', models.CharField(max_length=90, verbose_name='Organisation Type')),
            ],
        ),
        migrations.CreateModel(
            name='UserRoles',
            fields=[
                ('roleID', models.IntegerField(primary_key=True, serialize=False)),
                ('roleName', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name_plural': 'User Roles',
            },
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('userID', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=32, validators=[django.core.validators.MinLengthValidator(5)])),
                ('password', models.CharField(max_length=64, validators=[django.core.validators.MinLengthValidator(8)])),
                ('nickname', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('roleID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audit.userroles')),
            ],
            options={
                'verbose_name_plural': 'Users',
            },
        ),
        migrations.CreateModel(
            name='WasteEntries',
            fields=[
                ('wasteEntryID', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('userID', models.ForeignKey(db_column='userID', on_delete=django.db.models.deletion.CASCADE, to='audit.users')),
            ],
            options={
                'verbose_name_plural': 'Waste Entries',
            },
        ),
        migrations.CreateModel(
            name='WasteItems',
            fields=[
                ('wasteItemID', models.AutoField(primary_key=True, serialize=False)),
                ('itemDescription', models.CharField(max_length=64)),
                ('quantity', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('wasteEntryID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='audit.wasteentries')),
            ],
            options={
                'verbose_name_plural': 'Waste Items',
            },
        ),
        migrations.CreateModel(
            name='Donate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=7)),
                ('date', models.DateField()),
                ('orgID', models.ForeignKey(db_column='orgid', on_delete=django.db.models.deletion.CASCADE, to='audit.organisation')),
                ('userID', models.ForeignKey(db_column='userID', on_delete=django.db.models.deletion.CASCADE, to='audit.users')),
            ],
        ),
    ]
