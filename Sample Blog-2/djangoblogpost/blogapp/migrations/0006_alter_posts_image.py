# Generated by Django 4.1.3 on 2022-12-04 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_alter_posts_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]
