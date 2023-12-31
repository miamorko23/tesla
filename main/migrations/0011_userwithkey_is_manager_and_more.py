# Generated by Django 4.2.6 on 2023-12-01 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_userwithkey_address_userwithkey_phone_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='userwithkey',
            name='is_manager',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userwithkey',
            name='is_manager_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='userwithkey',
            name='secret_key',
            field=models.CharField(default='278c4392103262b40e15d68e7dd4bf5f', max_length=100),
        ),
    ]
