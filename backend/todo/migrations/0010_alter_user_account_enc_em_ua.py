# Generated by Django 3.2 on 2022-05-25 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0009_auto_20220525_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_account',
            name='enc_em_ua',
            field=models.CharField(blank=True, db_index=True, max_length=50, null=True, unique=True),
        ),
    ]