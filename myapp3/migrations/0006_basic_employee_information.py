# Generated by Django 4.2.dev20221108194129 on 2024-04-08 12:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myapp3", "0005_delete_book"),
    ]

    operations = [
        migrations.CreateModel(
            name="Basic_Employee_Information",
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
                ("Firstname", models.CharField(max_length=100)),
                ("Middlename", models.CharField(max_length=100)),
                ("Familyname", models.CharField(max_length=100)),
                ("Employeeid", models.IntegerField()),
                ("emailaddress", models.EmailField(max_length=100)),
                ("contact_number", models.BigIntegerField()),
                ("contact_number_length", models.PositiveSmallIntegerField(default=10)),
                ("country_code", models.CharField(blank=True, max_length=5, null=True)),
                ("Position", models.CharField(max_length=100)),
                ("Department", models.CharField(max_length=100)),
            ],
        ),
    ]
