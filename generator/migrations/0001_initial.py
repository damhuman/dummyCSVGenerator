# Generated by Django 3.1.2 on 2020-11-05 22:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CsvSeparator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('separator', models.CharField(max_length=1, unique=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Schema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('string_character', models.CharField(choices=[("'", "Single-quote(')"), ('"', 'Double-quote(")')], default='"', max_length=1)),
                ('date_modified', models.DateTimeField(auto_now_add=True)),
                ('column_separator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='generator.csvseparator')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SchemaColumn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_name', models.CharField(max_length=255)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'Full name'), (2, 'Integer'), (3, 'Job'), (4, 'Domain name'), (5, 'Phone number'), (6, 'Text'), (7, 'Date'), (8, 'Email'), (10, 'Company name')], default=1)),
                ('text_number_of_sentences', models.PositiveSmallIntegerField(default=1)),
                ('integer_range_from', models.PositiveSmallIntegerField(default=0)),
                ('integer_range_to', models.PositiveSmallIntegerField(default=1)),
                ('schema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='generator.schema')),
            ],
        ),
    ]
