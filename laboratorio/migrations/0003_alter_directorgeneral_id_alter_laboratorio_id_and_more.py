# Generated by Django 4.2.16 on 2024-12-03 22:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0002_directorgeneral'),
    ]

    operations = [
        migrations.AlterField(
            model_name='directorgeneral',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='laboratorio',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='producto',
            name='f_fabricacion',
            field=models.DateField(blank=True, default=datetime.date(2024, 12, 3), null=True),
        ),
        migrations.AlterField(
            model_name='producto',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
