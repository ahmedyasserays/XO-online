# Generated by Django 3.2.5 on 2021-08-12 23:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='global_message',
            name='unique_id',
            field=models.CharField(default=uuid.uuid4, max_length=100, unique=True),
        ),
    ]
