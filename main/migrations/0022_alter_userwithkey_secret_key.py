# Generated by Django 4.2.6 on 2023-12-05 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_alter_userwithkey_secret_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userwithkey',
            name='secret_key',
            field=models.CharField(default='7b8fb30bc8a3ddf4acc0db34ef763a99', max_length=100),
        ),
    ]
