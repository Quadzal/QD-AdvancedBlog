# Generated by Django 2.2.3 on 2019-09-30 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20190930_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Title'),
        ),
    ]
