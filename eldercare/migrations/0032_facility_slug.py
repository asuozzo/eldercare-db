# Generated by Django 2.2.7 on 2019-11-19 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eldercare', '0031_facility_formername'),
    ]

    operations = [
        migrations.AddField(
            model_name='facility',
            name='slug',
            field=models.SlugField(default='', editable=False, max_length=300),
        ),
    ]
