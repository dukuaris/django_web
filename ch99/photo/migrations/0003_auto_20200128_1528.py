# Generated by Django 2.2.2 on 2020-01-28 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0002_auto_20200125_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='SorlPhoto/%Y', verbose_name='IMAGE'),
        ),
    ]