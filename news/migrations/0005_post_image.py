# Generated by Django 4.2.10 on 2024-03-02 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_post_options_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='news/default.jpg', upload_to=''),
        ),
    ]
