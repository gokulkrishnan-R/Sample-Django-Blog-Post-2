# Generated by Django 4.1.3 on 2022-12-04 21:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0004_alter_comments_comment_body'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='posts',
            options={'ordering': ['posted_on']},
        ),
    ]