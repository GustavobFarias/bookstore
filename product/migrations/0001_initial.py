
# Generated by Django 3.2.8 on 2021-10-19 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("title", models.CharField(max_length=100)),
                ("slug", models.SlugField(unique=True)),
                (
                    "description",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("active", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("title", models.CharField(max_length=100)),
                (
                    "description",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
                ("price", models.PositiveIntegerField(null=True)),
                ("active", models.BooleanField(default=True)),
                (
                    "categories",
                    models.ManyToManyField(blank=True, to="product.Category"),
                ),
            ],
        ),
    ]

# Generated by Django 3.2.8 on 2021-10-19 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("title", models.CharField(max_length=100)),
                ("slug", models.SlugField(unique=True)),
                (
                    "description",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                ("active", models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("title", models.CharField(max_length=100)),
                (
                    "description",
                    models.TextField(blank=True, max_length=500, null=True),
                ),
                ("price", models.PositiveIntegerField(null=True)),
                ("active", models.BooleanField(default=True)),
                (
                    "categories",
                    models.ManyToManyField(blank=True, to="product.Category"),
                ),
            ],
        ),
    ]
