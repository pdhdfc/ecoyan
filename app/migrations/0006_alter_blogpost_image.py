# Generated by Django 5.0.6 on 2024-06-12 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0005_job_is_open"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="blog/images/"),
        ),
    ]