# Generated by Django 4.0.4 on 2022-06-19 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_gallery_is_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Would you like to show it?'),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='is_blog',
            field=models.BooleanField(default=False, verbose_name='Is it a blog?'),
        ),
    ]