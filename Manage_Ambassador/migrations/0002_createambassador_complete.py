# Generated by Django 2.1.4 on 2018-12-18 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Manage_Ambassador', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='createambassador',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
