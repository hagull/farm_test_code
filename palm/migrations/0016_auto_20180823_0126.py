# Generated by Django 2.0.7 on 2018-08-22 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('palm', '0015_auto_20180823_0108'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestHouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gcg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='palm.TestGcg')),
            ],
        ),
        migrations.AddField(
            model_name='testanode',
            name='house',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='palm.TestHouse'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testsnode',
            name='house',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, to='palm.TestHouse'),
            preserve_default=False,
        ),
    ]