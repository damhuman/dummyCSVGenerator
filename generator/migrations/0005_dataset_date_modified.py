# Generated by Django 3.1.2 on 2020-11-08 15:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0004_auto_20201108_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataset',
            name='date_modified',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]