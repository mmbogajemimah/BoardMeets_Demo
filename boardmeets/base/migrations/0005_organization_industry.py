# Generated by Django 4.2.2 on 2023-06-12 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_organization_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='industry',
            field=models.CharField(default=None, max_length=255),
        ),
    ]
