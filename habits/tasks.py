from datetime import datetime, timedelta
import requests

from celery import shared_task

from config.settings import TELEGRAM_BOT_API_KEY, TELEGRAM_CHAT_ID
from habits.models import Habit


@shared_task(name='send_message')
def send_message():
    url = f'https://api.telegram.org/bot{TELEGRAM_BOT_API_KEY}/sendMessage'
    param = {
        "text": 'Привет!',
        "chat_id": 979359063
    }
    response = requests.get(url, param)
    print(f'Сообщение в телеграм-бот отправлено')


# @shared_task(name='send_message')
# def send_message():
#     current_date = datetime.now().date()
#     current_time = datetime.now().time().strftime('%H:%M')
#
#     habits = Habit.objects.filter(is_pleasant=False)
#
#     for habit in habits:
#         period = habit.frequency
#         habit_start_date = habit.start.date()
#         habit_start_time = habit.start.time().strftime('%H:%M')
#
#         if habit_start_date <= current_date or habit.next_reminder_date == current_date:
#             if habit_start_time == current_time:
#                 url = f'https://api.telegram.org/bot{TELEGRAM_BOT_API_KEY}/sendMessage'
#                 param = {
#                     "text": f'Привет! {str(habit)}',
#                     "chat_id": TELEGRAM_CHAT_ID
#                 }
#                 response = requests.get(url, param)
#                 print(f'Сообщение в телеграм-бот отправлено. Подробнее:{response.json()}')
#
#             habit.next_reminder_date = current_date + timedelta(days=period)
#             habit.save()
