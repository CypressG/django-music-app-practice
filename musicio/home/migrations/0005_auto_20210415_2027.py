# Generated by Django 3.2 on 2021-04-15 17:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20210415_1819'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='price',
            field=models.FloatField(default=0),
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('FK_account', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('FK_song', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='home.song')),
            ],
        ),
    ]
