# Generated by Django 4.0.4 on 2022-05-21 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0017_book_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, default='defaultbook.jpeg', null=True, upload_to=''),
        ),
    ]