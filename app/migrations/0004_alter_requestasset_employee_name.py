# Generated by Django 3.2.9 on 2022-01-28 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_requestasset_asset_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestasset',
            name='employee_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]