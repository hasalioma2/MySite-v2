# Generated by Django 3.0.5 on 2020-05-14 20:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('toners', '0005_auto_20200426_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='toners',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]