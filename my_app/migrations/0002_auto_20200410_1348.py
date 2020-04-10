# Generated by Django 3.0.5 on 2020-04-10 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pizzashop',
            options={'verbose_name': 'Пиццерия', 'verbose_name_plural': 'Пиццерии'},
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название Пицца')),
                ('desc', models.TextField(verbose_name='Описание')),
                ('photo', models.ImageField(default='', upload_to='my_app/photos/', verbose_name='Фото')),
                ('pizzashop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_app.PizzaShop', verbose_name='Название Магазина')),
            ],
            options={
                'verbose_name': 'Пицца',
                'verbose_name_plural': 'Пиццы',
            },
        ),
    ]