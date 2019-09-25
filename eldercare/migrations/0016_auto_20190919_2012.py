# Generated by Django 2.2.5 on 2019-09-19 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eldercare', '0015_auto_20190919_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inspection',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='documentcloud_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inspection',
            name='state_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]