# Generated by Django 4.2.2 on 2023-06-12 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_organization_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='is_nonprofit',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='organization',
            name='social_media_facebook',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='social_media_instagram',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='social_media_linkedin',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='social_media_twitter',
            field=models.URLField(blank=True, null=True),
        ),
    ]
