# Generated by Django 3.2 on 2022-05-25 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_alter_user_account_enc_em_ua_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_account',
            old_name='user_account_name',
            new_name='username',
        ),
    ]
