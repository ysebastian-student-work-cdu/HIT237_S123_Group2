# Generated by Django 4.1.7 on 2023-05-31 09:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("audit", "0013_remove_users_roleid_alter_donate_userid_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="RecipesSaved",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Recipe", models.CharField(max_length=2000)),
            ],
        ),
    ]
