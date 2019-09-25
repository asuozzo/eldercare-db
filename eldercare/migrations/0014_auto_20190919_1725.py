# Generated by Django 2.2.5 on 2019-09-19 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eldercare', '0013_auto_20190919_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='allegation',
            name='allegation_num',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='allegation',
            name='seriousness',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='allegation',
            name='subcategory',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.CreateModel(
            name='Penalties',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('penalty', models.IntegerField(blank=True, null=True)),
                ('facility', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='eldercare.Facility')),
            ],
        ),
    ]