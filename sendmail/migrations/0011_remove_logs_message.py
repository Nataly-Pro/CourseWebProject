# Generated by Django 4.2.7 on 2023-12-10 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sendmail', '0010_remove_logs_response'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='logs',
            name='message',
        ),
    ]
