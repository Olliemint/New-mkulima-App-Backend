# Generated by Django 4.0.6 on 2022-07-13 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_category_comment_profile_merchandise_feeds_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default='mkulima', max_length=255, unique=True),
        ),
    ]