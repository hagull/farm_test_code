# Generated by Django 2.0.7 on 2018-08-22 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('palm', '0013_auto_20180815_1611'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestAnode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anode_id', models.IntegerField()),
                ('anode_value', models.IntegerField(default=None)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('gcg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='palm.Gcg')),
            ],
        ),
        migrations.CreateModel(
            name='TestGcg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gcg_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TestSnode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('snode_id', models.IntegerField()),
                ('snode_value', models.IntegerField(default=None)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('gcg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='palm.TestGcg')),
            ],
        ),
    ]