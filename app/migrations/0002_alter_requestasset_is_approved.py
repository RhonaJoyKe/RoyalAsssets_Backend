# Generated by Django 3.2.7 on 2022-02-01 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestasset',
            name='is_approved',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Declined', 'Declined')], default='Pending', max_length=50, null=True),
        ),
    ]
