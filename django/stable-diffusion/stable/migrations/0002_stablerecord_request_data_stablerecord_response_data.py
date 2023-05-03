# Generated by Django 4.2 on 2023-05-03 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stable', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stablerecord',
            name='request_data',
            field=models.JSONField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='stablerecord',
            name='response_data',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
