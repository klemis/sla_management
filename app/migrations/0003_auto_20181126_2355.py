# Generated by Django 2.1.3 on 2018-11-26 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20181126_2349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operator',
            name='country',
            field=models.CharField(max_length=100),
        ),
    ]
