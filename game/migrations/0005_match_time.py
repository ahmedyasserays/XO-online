# Generated by Django 3.2.5 on 2021-09-16 20:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_alter_match_draw'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]