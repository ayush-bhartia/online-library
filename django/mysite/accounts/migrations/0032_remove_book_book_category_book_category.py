# Generated by Django 4.0.4 on 2022-06-03 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0031_rename_category_book_book_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_category',
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.CharField(choices=[('Thriller', 'Thriller'), ('Horror', 'Horror'), ('Knowledge', 'Knowlegde')], max_length=200, null=True),
        ),
    ]
