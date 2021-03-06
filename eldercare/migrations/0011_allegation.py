# Generated by Django 2.2.5 on 2019-09-19 17:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eldercare', '0010_complaint'),
    ]

    operations = [
        migrations.CreateModel(
            name='Allegation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=300, null=True)),
                ('complaint', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='eldercare.Complaint')),
                ('facility', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='eldercare.Facility')),
            ],
        ),
    ]
