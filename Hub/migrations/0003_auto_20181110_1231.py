# Generated by Django 2.1.3 on 2018-11-10 12:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hub', '0002_hubmanager_order_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hubmanager',
            old_name='order_id',
            new_name='order',
        ),
    ]
