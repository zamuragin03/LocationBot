# Generated by Django 4.2.4 on 2023-09-19 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_actiontype_options_alter_location_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='useraction',
            options={'verbose_name': 'Действие пользователя', 'verbose_name_plural': 'Действия пользователей'},
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='is_notificated',
            field=models.BooleanField(default=True),
        ),
    ]
