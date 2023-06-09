# Generated by Django 4.1 on 2022-08-18 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_me', models.CharField(max_length=250, null=True)),
                ('birthday', models.DateField(null=True)),
                ('profile_pic', models.ImageField(upload_to='profile_images')),
                ('cover_pic', models.ImageField(upload_to='cover_images')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=6, null=True)),
            ],
        ),
    ]
