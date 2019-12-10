# Generated by Django 2.2.7 on 2019-11-25 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eldercare', '0033_inspection_under_appeal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facility',
            name='in_business',
            field=models.BooleanField(blank=True, default=True, null=True),
        ),
        migrations.AlterField(
            model_name='penalty',
            name='penalty',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]