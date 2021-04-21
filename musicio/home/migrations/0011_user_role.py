# Generated by Django 3.2 on 2021-04-17 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20210417_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Publisher'), (2, 'Moderator')], null=True),
        ),
    ]