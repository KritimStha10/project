# Generated by Django 4.1.5 on 2023-01-27 06:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.DeleteModel(
            name='EmailTokens',
        ),
        migrations.RemoveField(
            model_name='phonetokens',
            name='phone',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='PhoneTokens',
        ),
    ]