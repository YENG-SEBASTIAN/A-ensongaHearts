# Generated by Django 4.2.6 on 2023-10-13 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aensongaApp', '0002_fact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cause',
            name='caption',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='homeslideshowimage',
            name='caption',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='president',
            name='about_me',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='projectgallary',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
