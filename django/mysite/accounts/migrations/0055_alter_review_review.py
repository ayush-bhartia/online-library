# Generated by Django 4.0.6 on 2022-07-24 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0054_customerquery_delete_query'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='Review',
            field=models.TextField(max_length=2000, null=True),
        ),
    ]
