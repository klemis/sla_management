# Generated by Django 2.1.3 on 2018-12-03 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20181130_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operator',
            name='country',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Country'),
        ),
    ]
