# Generated by Django 2.2.5 on 2019-09-18 17:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eldercare', '0003_auto_20190918_1713'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facility',
            name='capacity',
        ),
    ]
