# Generated by Django 2.1.5 on 2019-05-03 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_ratingvalues'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratingvalues',
            name='id',
        ),
        migrations.AlterField(
            model_name='ratingvalues',
            name='value',
            field=models.IntegerField(default=0, primary_key=True, serialize=False),
        ),
    ]