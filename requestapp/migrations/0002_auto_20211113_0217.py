# Generated by Django 3.2.7 on 2021-11-12 17:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('requestapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quest',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
        migrations.AlterField(
            model_name='quest',
            name='end_price',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='quest',
            name='start_price',
            field=models.IntegerField(default=1),
        ),
    ]