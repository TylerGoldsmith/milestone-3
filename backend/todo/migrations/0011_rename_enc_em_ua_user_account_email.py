# Generated by Django 3.2 on 2022-05-25 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0010_alter_user_account_enc_em_ua'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_account',
            old_name='enc_em_ua',
            new_name='email',
        ),
    ]