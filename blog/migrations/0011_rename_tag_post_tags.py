# Generated by Django 4.2 on 2023-05-15 14:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0010_tag_post_tag"),
    ]

    operations = [
        migrations.RenameField(
            model_name="post",
            old_name="tag",
            new_name="tags",
        ),
    ]
