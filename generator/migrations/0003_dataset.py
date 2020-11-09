# Generated by Django 3.1.2 on 2020-11-08 12:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0002_schemacolumn_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row_count', models.IntegerField(default=10)),
                ('schema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='generator.schema')),
            ],
        ),
    ]