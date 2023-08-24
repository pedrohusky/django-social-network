# Generated by Django 4.2.4 on 2023-08-20 06:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('developers', '0009_remove_userprofile_blocked_users_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='relationships',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='friends',
            field=models.ManyToManyField(blank=True, related_name='user_friends', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Relationship',
        ),
    ]