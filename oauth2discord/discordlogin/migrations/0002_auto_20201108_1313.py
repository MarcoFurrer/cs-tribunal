# Generated by Django 3.1.2 on 2020-11-08 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discordlogin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discorduser',
            name='flags',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='discorduser',
            name='public_flags',
            field=models.IntegerField(),
        ),
    ]