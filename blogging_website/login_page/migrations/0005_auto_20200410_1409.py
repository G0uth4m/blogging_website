# Generated by Django 2.2.4 on 2020-04-10 08:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_page', '0004_auto_20200410_1402'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='username',
            new_name='name',
        ),
    ]
