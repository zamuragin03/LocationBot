# Generated by Django 4.2.4 on 2023-09-08 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actiontype',
            options={'verbose_name': 'Тип действия', 'verbose_name_plural': 'Типы действий'},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name': 'Филиал', 'verbose_name_plural': 'Филиалы'},
        ),
        migrations.AlterField(
            model_name='telegramuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Имя в тг'),
        ),
        migrations.AlterField(
            model_name='telegramuser',
            name='second_name',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Фамилия в тг'),
        ),
        migrations.AlterField(
            model_name='telegramuser',
            name='username',
            field=models.CharField(blank=True, max_length=256, null=True, verbose_name='Ник в тг'),
        ),
    ]
