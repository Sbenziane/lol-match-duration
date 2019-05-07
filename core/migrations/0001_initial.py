# Generated by Django 2.1.7 on 2019-02-25 07:20

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields
import picklefield.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('api_id', models.IntegerField()),
                ('rq_job_id', models.UUIDField(null=True)),
                ('raw_info', jsonfield.fields.JSONField(null=True)),
                ('started_at', models.DateTimeField()),
                ('ended_at', models.DateTimeField(blank=True, null=True)),
                ('predicted_ended_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'matches',
                'db_table': 't_matches',
            },
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.TextField(unique=True)),
                ('pipeline', picklefield.fields.PickledObjectField(editable=False)),
            ],
            options={
                'verbose_name_plural': 'models',
                'db_table': 't_models',
            },
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('short_name', models.TextField()),
                ('full_name', models.TextField()),
                ('platform', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'regions',
                'db_table': 't_regions',
            },
        ),
        migrations.AddField(
            model_name='match',
            name='predicted_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Model'),
        ),
        migrations.AddField(
            model_name='match',
            name='region',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Region'),
        ),
    ]