# Generated by Django 4.0.4 on 2022-08-19 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Social_Media_App', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='about_me',
            new_name='desc',
        ),
        migrations.RemoveField(
            model_name='post',
            name='birthday',
        ),
        migrations.RemoveField(
            model_name='post',
            name='cover_pic',
        ),
        migrations.RemoveField(
            model_name='post',
            name='gender',
        ),
        migrations.AddField(
            model_name='post',
            name='date_time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
