# Generated by Django 4.2.2 on 2023-06-21 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_alter_organization_stuff_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='phone_number',
            field=models.CharField(max_length=200),
        ),
    ]
