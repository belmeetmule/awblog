# Generated by Django 4.2.6 on 2023-10-26 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='featured_image/%Y/%m/%d/'),
        ),
    ]
