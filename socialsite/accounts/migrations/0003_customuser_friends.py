# Generated by Django 5.0.3 on 2024-06-12 10:37

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0002_friendrequest_post_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="friends",
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
