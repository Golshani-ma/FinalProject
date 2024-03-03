# Generated by Django 4.2.10 on 2024-02-29 19:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_rename_news_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='counted_views',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='login_required',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='published_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='updated_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]