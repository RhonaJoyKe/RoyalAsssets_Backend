# Generated by Django 3.2.9 on 2022-01-28 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_request_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
