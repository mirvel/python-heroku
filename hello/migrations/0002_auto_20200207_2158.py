# Generated by Django 3.0.3 on 2020-02-07 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='greeting',
            name='when',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date created'),
        ),
    ]
