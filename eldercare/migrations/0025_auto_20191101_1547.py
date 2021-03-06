# Generated by Django 2.2.6 on 2019-11-01 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eldercare', '0024_auto_20191101_1539'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='citation',
            name='scope',
        ),
        migrations.RemoveField(
            model_name='citation',
            name='severity',
        ),
        migrations.AddField(
            model_name='citation',
            name='citation_subtype',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='citation',
            name='severity_scope',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='eldercare.Severity_Scope'),
        ),
    ]
