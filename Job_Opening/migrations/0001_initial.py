# Generated by Django 5.0.1 on 2024-01-24 09:10

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Job_Opening",
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
                ("NameofCompany", models.CharField(max_length=200)),
                ("profileOfCompany", models.CharField(max_length=200)),
                ("JobProfile", models.CharField(max_length=100)),
                (
                    "BranchChoice",
                    models.CharField(
                        choices=[
                            ("CSE", "Computer Science and Engineering"),
                            ("ECE", "Electronics and Engineering"),
                        ],
                        max_length=50,
                    ),
                ),
                ("ctc", models.TextField()),
                ("Eligibility", models.TextField()),
                (
                    "Selection",
                    models.CharField(
                        choices=[("Virtual", "Virtual"), ("Offline", "Offline")],
                        max_length=10,
                    ),
                ),
                ("location", models.CharField(max_length=100)),
                ("stipend", models.IntegerField()),
                ("start", models.DateField()),
            ],
        ),
    ]
