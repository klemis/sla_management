# Generated by Django 2.1.3 on 2018-11-26 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='operator',
            options={},
        ),
        migrations.RenameField(
            model_name='operator',
            old_name='operator_name',
            new_name='operator',
        ),
    ]
