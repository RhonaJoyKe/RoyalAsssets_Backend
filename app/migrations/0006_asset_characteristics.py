# Generated by Django 3.2.9 on 2022-01-26 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20220126_0557'),
    ]

    operations = [
        migrations.CreateModel(
            name='Characteristics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Character_name', models.CharField(max_length=20, null=True)),
                ('quantity', models.PositiveIntegerField(null=True)),
                ('category', models.CharField(choices=[('Stationary', 'Stationary'), ('Electronics', 'Electronics'), ('Furniture', 'Furniture')], max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asset_name', models.CharField(max_length=100, null=True)),
                ('asset_value', models.PositiveIntegerField(null=True)),
                ('Character_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.characteristics')),
            ],
        ),
    ]
