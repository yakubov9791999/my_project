# Generated by Django 3.0.5 on 2020-04-11 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indexpage', '0003_article_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='likes',
        ),
    ]
