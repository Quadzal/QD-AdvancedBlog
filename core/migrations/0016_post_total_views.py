# Generated by Django 2.2.3 on 2019-10-30 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_remove_userprofile_favourite_posts'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='total_views',
            field=models.IntegerField(default=0),
        ),
    ]