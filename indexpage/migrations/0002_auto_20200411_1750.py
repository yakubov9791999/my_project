# Generated by Django 3.0.5 on 2020-04-11 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexpage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='type',
            field=models.IntegerField(choices=[(1, 'Type 1'), (2, 'Type 2')]),
        ),
    ]