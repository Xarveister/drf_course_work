from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Habit(models.Model):
    """ Модель привычки """

    action = models.CharField(max_length=150, verbose_name='Действие')
    start = models.DateTimeField(verbose_name='Время и дата начала')
    frequency = models.SmallIntegerField(default=7, verbose_name='Периодичность выполнения')
    next_reminder_date = models.DateField(**NULLABLE, verbose_name='Дата следующего напоминания')
    time_to_complete = models.DurationField(verbose_name='Время выполнения')
    place = models.CharField(max_length=150, verbose_name='Место')

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь')

    related_habit = models.ForeignKey('Habit', on_delete=models.SET_NULL, **NULLABLE)
    reward = models.CharField(max_length=150, **NULLABLE, verbose_name='Вознаграждение')

    is_public = models.BooleanField(default=False, verbose_name='Публичная')
    is_pleasant = models.BooleanField(default=False, verbose_name='Приятная')

    def __str__(self):
        return f'{self.action} в {self.start} {self.place}'

    class Meta:
        verbose_name = 'Привычка'
        verbose_name_plural = 'Привычки'
        ordering = ['start']
