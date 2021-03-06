# Generated by Django 2.1.7 on 2019-02-19 19:58

import datetime
from django.db import migrations, models
import django.db.models.deletion
import evidence.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('directory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EvidenceSummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=datetime.datetime(2019, 2, 19, 19, 58, 29, 460550), editable=False, verbose_name='Created at')),
                ('updated', models.DateTimeField(default=datetime.datetime(2019, 2, 19, 19, 58, 29, 460591), editable=False, verbose_name='Updated at')),
                ('language', models.CharField(choices=[('en', 'English'), ('pt-br', 'Brazilian Portuguese'), ('es', 'Spanish')], default='en', max_length=10, verbose_name='language')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('context', models.TextField(blank=True, null=True, verbose_name='Context')),
                ('question', models.CharField(blank=True, max_length=255, null=True, verbose_name='Question')),
                ('link', models.URLField(blank=True, verbose_name='link')),
                ('file', models.FileField(blank=True, upload_to=evidence.models.EvidenceSummary.new_filename, verbose_name='File')),
            ],
            options={
                'verbose_name': 'Evidence Summary',
                'verbose_name_plural': 'Evidence Summaries',
            },
        ),
        migrations.CreateModel(
            name='EvidenceSummaryLocal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language', models.CharField(choices=[('en', 'English'), ('pt-br', 'Brazilian Portuguese'), ('es', 'Spanish')], max_length=10, verbose_name='language')),
                ('created', models.DateTimeField(default=datetime.datetime(2019, 2, 19, 19, 58, 29, 461460), editable=False, verbose_name='Created at')),
                ('updated', models.DateTimeField(default=datetime.datetime(2019, 2, 19, 19, 58, 29, 461493), editable=False, verbose_name='Updated at')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('context', models.TextField(blank=True, null=True, verbose_name='Context')),
                ('question', models.CharField(blank=True, max_length=255, null=True, verbose_name='Question')),
                ('link', models.URLField(blank=True, verbose_name='link')),
                ('file', models.FileField(blank=True, upload_to=evidence.models.EvidenceSummaryLocal.new_filename, verbose_name='File')),
                ('evidence', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='evidence.EvidenceSummary')),
            ],
            options={
                'verbose_name': 'Evidence Summary Translate',
                'verbose_name_plural': 'Evidence Summary Translations',
            },
        ),
        migrations.CreateModel(
            name='MedicineEvidenceSummary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evidence', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='evidence.EvidenceSummary')),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='directory.Medicine')),
            ],
            options={
                'verbose_name': 'Evidence Summary in Medicine',
                'verbose_name_plural': 'Evidence Summaries in Medicine',
            },
        ),
    ]
