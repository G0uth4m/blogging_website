# Generated by Django 2.2.4 on 2020-04-10 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_page', '0006_auto_20200410_1412'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='username1',
        ),
    ]
