# Generated by Django 2.0.7 on 2018-08-15 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('palm', '0012_auto_20180815_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opranode',
            name='priority',
            field=models.IntegerField(),
        ),
    ]
