# Generated by Django 2.1.2 on 2018-11-06 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carton', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='end_time',
            field=models.DateTimeField(auto_now_add=True, help_text='Enter when the class ends'),
        ),
        migrations.AlterField(
            model_name='session',
            name='start_time',
            field=models.DateTimeField(auto_now_add=True, help_text='Enter when the class starts'),
        ),
    ]
