# Generated by Django 2.2.2 on 2020-01-09 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='created_dt',
            new_name='create_dt',
        ),
    ]
