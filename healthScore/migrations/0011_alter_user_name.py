# Generated by Django 4.2 on 2024-03-09 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("healthScore", "0010_alter_user_dob"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="name",
            field=models.TextField(max_length=255),
        ),
    ]
