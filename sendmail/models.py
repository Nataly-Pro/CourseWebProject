from datetime import datetime

from django.conf import settings
from django.db import models
from django.utils import timezone

NULLABLE = {'null': True, 'blank': True}
STATUS_CHOICES = [
    ('Создана', 'Создана'),
    ('Активна', 'Активна'),
    ('Завершена', 'Завершена'),
]
INTERVAL_CHOICES = [
    ('ежедневно', 'ежедневно'),
    ('раз в неделю', 'раз в неделю'),
    ('раз в месяц', 'раз в месяц'),
]


class Client(models.Model):
    full_name = models.CharField(max_length=150, verbose_name='ФИО')
    email = models.EmailField(verbose_name='почта')
    comment = models.TextField(verbose_name='комментарий', **NULLABLE)

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Message(models.Model):
    title = models.CharField(max_length=250, verbose_name='тема')
    content = models.TextField(verbose_name='содержание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'сообщение'
        verbose_name_plural = 'сообщения'


class Mailing(models.Model):
    name = models.CharField(max_length=50, verbose_name='название рассылки')
    mail_to = models.ManyToManyField(Client, verbose_name='кому')
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='сообщение', **NULLABLE)
    start_date = models.DateTimeField(default=timezone.now, verbose_name='время старта рассылки')
    next_date = models.DateTimeField(default=start_date, verbose_name='время следующей рассылки')
    end_date = models.DateTimeField(verbose_name='время окончания рассылки')
    interval = models.CharField(max_length=50, choices=INTERVAL_CHOICES, verbose_name='периодичность')
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, help_text="Выберите Создана или Завершена")

    def __str__(self):
        return f'"{self.name}"'

    class Meta:
        verbose_name = 'рассылка'
        verbose_name_plural = 'рассылки'


class Logs(models.Model):
    message = models.ForeignKey(Message, on_delete=models.SET_NULL, verbose_name='сообщение', **NULLABLE)
    last_mailing_time = models.DateTimeField(auto_now=True, verbose_name='время последней рассылки')
    status = models.CharField(max_length=50, verbose_name='статус попытки', null=True)
    response = models.TextField(verbose_name='ответ сервера', default=None, null=True)

    class Meta:
        verbose_name = 'log'
        verbose_name_plural = 'logs'



