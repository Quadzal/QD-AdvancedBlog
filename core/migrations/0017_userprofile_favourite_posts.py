# Generated by Django 2.2.3 on 2019-11-16 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_post_total_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='favourite_posts',
            field=models.ManyToManyField(to='core.Post'),
        ),
    ]