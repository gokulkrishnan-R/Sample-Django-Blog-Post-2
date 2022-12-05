# Generated by Django 4.1.3 on 2022-12-02 03:43

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('comment_body', models.CharField(default='some string', max_length=256, null=True)),
                ('posted_on', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.BooleanField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blogapp.posts')),
            ],
            options={
                'ordering': ['posted_on'],
            },
        ),
    ]
