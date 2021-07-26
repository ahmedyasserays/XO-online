# Generated by Django 3.2.5 on 2021-07-26 12:14

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20210726_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='front_id',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
