# Generated by Django 4.2.6 on 2023-10-18 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aensongaApp', '0003_alter_cause_caption_alter_homeslideshowimage_caption_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cause',
            name='targetAmount',
        ),
    ]
