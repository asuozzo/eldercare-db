# Generated by Django 2.2.5 on 2019-09-19 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eldercare', '0014_auto_20190919_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facility',
            name='capacity',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]