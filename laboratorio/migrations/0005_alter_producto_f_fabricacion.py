# Generated by Django 4.2.16 on 2024-12-03 22:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('laboratorio', '0004_alter_directorgeneral_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='f_fabricacion',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
