# Generated by Django 2.0.7 on 2018-08-08 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('palm', '0005_auto_20180808_1851'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gcg',
            old_name='cctv_num',
            new_name='cctv_outside_num',
        ),
        migrations.AddField(
            model_name='gcg',
            name='cctv_inside_num',
            field=models.IntegerField(default=None),
            preserve_default=False,
        ),
    ]