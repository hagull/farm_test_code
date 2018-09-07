# Generated by Django 2.0.7 on 2018-08-02 11:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Anode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anode_id', models.IntegerField(unique=True)),
                ('priority', models.IntegerField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='AnodeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sw_version', models.CharField(max_length=50)),
                ('register_id', models.IntegerField()),
                ('register_date', models.DateTimeField(auto_now_add=True)),
                ('node_status', models.CharField(max_length=50)),
                ('opr_status', models.CharField(max_length=100)),
                ('monitor', models.CharField(max_length=50)),
                ('set_vlaue', models.CharField(blank=True, max_length=100)),
                ('comm_err_num', models.IntegerField()),
                ('service_err_num', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('anode', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='palm.Anode')),
            ],
        ),
        migrations.CreateModel(
            name='Emergency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('u_value', models.FloatField()),
                ('r_value', models.FloatField()),
                ('l_value', models.FloatField()),
                ('priority', models.IntegerField(unique=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('anode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='palm.Anode')),
            ],
        ),
        migrations.CreateModel(
            name='Gcg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gcg_id', models.IntegerField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='GcgInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('snode_num', models.IntegerField()),
                ('data_period', models.DateTimeField()),
                ('anode_num', models.IntegerField()),
                ('ipv4', models.CharField(max_length=100)),
                ('ipv6', models.CharField(max_length=100)),
                ('version', models.CharField(max_length=50)),
                ('mcu', models.CharField(max_length=50)),
                ('os', models.CharField(max_length=50)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('gcg', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='palm.Gcg')),
            ],
        ),
        migrations.CreateModel(
            name='Operating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opr_type', models.CharField(max_length=100)),
                ('opr_comment', models.TextField()),
                ('snode_num', models.IntegerField()),
                ('anode_num', models.IntegerField()),
                ('u_value', models.FloatField()),
                ('r_value', models.FloatField()),
                ('l_value', models.FloatField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('gcg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='palm.Gcg')),
            ],
        ),
        migrations.CreateModel(
            name='OprAnode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.IntegerField(unique=True)),
                ('anode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='palm.Anode')),
                ('operating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='palm.Operating')),
            ],
        ),
        migrations.CreateModel(
            name='OprSnode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='palm.Operating')),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('house_num', models.IntegerField()),
                ('joined_at', models.DateTimeField(auto_now_add=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='palm.Address')),
            ],
        ),
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vegi_size', models.FloatField()),
                ('vegi_condition', models.CharField(max_length=50)),
                ('vegi_cultivation', models.CharField(choices=[('s', '재배 시작'), ('i', '재배중'), ('e', '재배 종료')], max_length=1)),
                ('vegi_shipment', models.FloatField()),
                ('vegi_comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Snode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('snode_id', models.IntegerField(unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('gcg', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='palm.Gcg')),
            ],
        ),
        migrations.CreateModel(
            name='SnodeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sw_version', models.CharField(max_length=50)),
                ('register_id', models.IntegerField()),
                ('register_date', models.DateTimeField(auto_now_add=True)),
                ('node_status', models.CharField(max_length=50)),
                ('monitor', models.CharField(max_length=50)),
                ('set_vlaue', models.CharField(blank=True, max_length=100)),
                ('comm_err_num', models.IntegerField()),
                ('service_err_num', models.IntegerField()),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('snode', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='palm.Snode')),
            ],
        ),
        migrations.CreateModel(
            name='VegiType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vegi_type', models.CharField(choices=[('a', '오이'), ('b', '딸기'), ('c', '더덕')], max_length=1)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='daily_set', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='record',
            name='vegi_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='palm.VegiType'),
        ),
        migrations.AddField(
            model_name='oprsnode',
            name='snode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='palm.Snode'),
        ),
        migrations.AddField(
            model_name='gcg',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='palm.Owner'),
        ),
        migrations.AddField(
            model_name='emergency',
            name='emergency_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='palm.Snode'),
        ),
        migrations.AddField(
            model_name='anodeinfo',
            name='emergency_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='palm.Snode'),
        ),
        migrations.AddField(
            model_name='anode',
            name='gcg',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='palm.Gcg'),
        ),
    ]