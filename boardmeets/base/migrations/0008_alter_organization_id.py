# Generated by Django 4.2.2 on 2023-06-13 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_alter_organization_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organization',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
