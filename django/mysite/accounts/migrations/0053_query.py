# Generated by Django 4.0.4 on 2022-06-24 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0052_book_downvote_alter_book_upvote'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('query', models.TextField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]
