# Generated by Django 2.1.3 on 2018-11-20 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Manage_Call_Center', '0003_handlerequest'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]