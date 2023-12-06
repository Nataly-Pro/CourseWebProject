# Generated by Django 4.2.7 on 2023-12-06 03:15

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('sendmail', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailing',
            name='next_date',
            field=models.DateTimeField(default=models.DateTimeField(default=django.utils.timezone.now, verbose_name='время старта рассылки'), verbose_name='время следующей рассылки'),
        ),
        migrations.AlterField(
            model_name='mailing',
            name='start_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='время старта рассылки'),
        ),
    ]
