# Generated by Django 4.2.7 on 2023-12-07 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sendmail', '0003_alter_mailing_next_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailing',
            options={'ordering': ('start_date',), 'verbose_name': 'рассылка', 'verbose_name_plural': 'рассылки'},
        ),
    ]