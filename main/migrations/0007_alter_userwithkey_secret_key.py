# Generated by Django 4.2.6 on 2023-11-20 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_userwithkey_secret_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userwithkey',
            name='secret_key',
            field=models.CharField(default='8e2609dec4ad4d4cd5fc1713ee6922d0', max_length=100),
        ),
    ]