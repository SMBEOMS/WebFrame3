# Generated by Django 4.2 on 2023-04-24 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("single_pages", "0005_alter_student_head_image"),
    ]

    operations = [
        migrations.RenameField(
            model_name="student",
            old_name="head_image",
            new_name="image",
        ),
    ]
