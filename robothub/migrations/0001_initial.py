# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('application_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('application_name', models.CharField(max_length=100)),
                ('framework_name', models.CharField(max_length=200)),
                ('jira_link', models.CharField(max_length=200)),
                ('git_link', models.CharField(max_length=200)),
                ('project_id', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Keyword',
            fields=[
                ('keyword_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=500)),
                ('doc', models.IntegerField()),
                ('timeout', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=20)),
                ('test_id', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='KeywordArguments',
            fields=[
                ('keyword_arguments_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('content', models.CharField(max_length=500)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='KeywordMessages',
            fields=[
                ('keyword_message_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('content', models.CharField(max_length=500)),
                ('timestamp', models.DateTimeField()),
                ('level', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='KeywordStatus',
            fields=[
                ('keyword_status_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('status', models.CharField(max_length=500)),
                ('elasped', models.IntegerField()),
                ('test_run_id', models.CharField(max_length=20)),
                ('keyword_id', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_id', models.IntegerField(max_length=20, serialize=False, primary_key=True)),
                ('project_name', models.CharField(max_length=100)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Suite',
            fields=[
                ('suite_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('source', models.CharField(max_length=500)),
                ('xml_id', models.IntegerField()),
                ('name', models.CharField(max_length=500)),
                ('doc', models.CharField(max_length=2000)),
                ('application_id', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SuiteStatus',
            fields=[
                ('suite_status_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('status', models.CharField(max_length=500)),
                ('failed', models.IntegerField()),
                ('elasped', models.IntegerField()),
                ('passed', models.IntegerField()),
                ('test_run_id', models.CharField(max_length=20)),
                ('suite_id', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('tag_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('content', models.CharField(max_length=200)),
                ('test_id', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TagStatus',
            fields=[
                ('tag_status_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=500)),
                ('failed', models.IntegerField()),
                ('elasped', models.IntegerField()),
                ('critical', models.IntegerField()),
                ('passed', models.IntegerField()),
                ('test_run_id', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('test_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('source', models.CharField(max_length=500)),
                ('xml_id', models.IntegerField()),
                ('name', models.CharField(max_length=500)),
                ('doc', models.CharField(max_length=2000)),
                ('timeout', models.CharField(max_length=10)),
                ('suite_id', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestRun',
            fields=[
                ('test_run_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('started_at', models.DateTimeField()),
                ('finished_at', models.DateTimeField()),
                ('source_file', models.CharField(max_length=500)),
                ('hash', models.CharField(max_length=50)),
                ('imported_at', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestRunError',
            fields=[
                ('test_run_error_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('content', models.CharField(max_length=500)),
                ('timestamp', models.DateTimeField()),
                ('level', models.CharField(max_length=20)),
                ('test_run_id', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestRunStatus',
            fields=[
                ('test_run_status_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('passed', models.IntegerField()),
                ('name', models.CharField(max_length=500)),
                ('failed', models.IntegerField()),
                ('elasped', models.IntegerField()),
                ('test_run_id', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TestStatus',
            fields=[
                ('test_status_id', models.CharField(max_length=20, serialize=False, primary_key=True)),
                ('status', models.CharField(max_length=20)),
                ('elasped', models.IntegerField()),
                ('test_id', models.CharField(max_length=20)),
                ('test_run_id', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
