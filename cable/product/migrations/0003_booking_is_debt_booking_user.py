# Generated by Django 5.0 on 2023-12-19 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_booking'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='is_debt',
            field=models.CharField(default=False, max_length=50),
        ),
        migrations.AddField(
            model_name='booking',
            name='user',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
