# Generated by Django 4.2.6 on 2023-11-19 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_userwithkey_secret_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userwithkey',
            name='secret_key',
            field=models.CharField(default='fcce7b0bc9196c367ac46647e599bd22', max_length=100),
        ),
    ]
