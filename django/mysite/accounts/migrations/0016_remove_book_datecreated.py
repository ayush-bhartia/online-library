# Generated by Django 4.0.4 on 2022-05-21 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_customer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='datecreated',
        ),
    ]
