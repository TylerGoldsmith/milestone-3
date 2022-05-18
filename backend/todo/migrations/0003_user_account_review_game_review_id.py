# Generated by Django 4.0.4 on 2022-05-17 22:43

from django.db import migrations, models
import django.db.models.deletion
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_game_game_platform_game_publisher_genre_platform_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_Account',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('user_account_name', models.CharField(max_length=100)),
                ('enc_em_ua', django_cryptography.fields.encrypt(models.CharField(max_length=30))),
                ('enc_pw_ua', django_cryptography.fields.encrypt(models.CharField(max_length=25))),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('review', models.TextField(max_length=100)),
                ('user_account_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todo.user_account')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='review_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='todo.review'),
        ),
    ]
