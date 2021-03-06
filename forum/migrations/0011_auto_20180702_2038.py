# Generated by Django 2.0.4 on 2018-07-02 14:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0010_forumsection_section_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='updated_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
