# Generated by Django 2.2.6 on 2019-10-11 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eldercare', '0019_auto_20190930_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='facility',
            name='lat',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='facility',
            name='lon',
            field=models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True),
        ),
    ]
