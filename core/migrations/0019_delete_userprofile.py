# Generated by Django 2.2.3 on 2019-12-20 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_userprofile_favourite_comments'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]