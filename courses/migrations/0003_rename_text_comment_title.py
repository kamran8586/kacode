# Generated by Django 5.0 on 2023-12-18 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='text',
            new_name='title',
        ),
    ]
