from datetime import timedelta

from rest_framework.exceptions import ValidationError


class RelatedHabitOrRewardValidator:
    """ Исключает одновременный выбор связанной привычки и вознаграждения """

    def __init__(self, related_habit_field, reward_field):
        self.related_habit_field = related_habit_field
        self.reward_field = reward_field

    def __call__(self, values):
        related_habit = values.get(self.related_habit_field)
        reward = values.get(self.reward_field)
        if related_habit and reward:
            raise ValidationError('Необходимо выбрать связанную привычку ИЛИ вознаграждение')


class TimeToCompleteLimitationValidator:
    """ Ограничивает время выполнения привычки """

    def __init__(self, time_to_complete_field):
        self.time_to_complete_field = time_to_complete_field

    def __call__(self, value):
        time_to_complete = value.get(self.time_to_complete_field)
        if time_to_complete > timedelta(seconds=120):
            raise ValidationError('Время выполнения привычки НЕ должно превышать 120 секунд')


class RelatedHabitValidation:
    """ В связанные привычки попадают только приятные привычки """

    def __init__(self, related_habit_field):
        self.related_habit_field = related_habit_field

    def __call__(self, value):
        related_habit = value.get(self.related_habit_field)

        if related_habit:
            if not related_habit.is_pleasant:
                raise ValidationError('Связанная привычка может быть ТОЛЬКО приятной')


class PleasantHabitValidation:
    """ Приятная привычка не имеет вознаграждения или другой связанной привычки """

    def __init__(self, related_habit_field, is_pleasant_field, reward_field):
        self.related_habit_field = related_habit_field
        self.is_pleasant_field = is_pleasant_field
        self.reward_field = reward_field

    def __call__(self, values):
        related_habit = values.get(self.related_habit_field)
        reward = values.get(self.reward_field)
        is_pleasant = values.get(self.is_pleasant_field)
        if is_pleasant and related_habit:
            raise ValidationError('Приятная привычка НЕ может иметь связанной привычки')
        elif is_pleasant and reward:
            raise ValidationError('Приятная привычка НЕ может иметь вознаграждения')


class FrequencyValidation:
    """ Привычка выполняется не реже, чем 1 раз в 7 дней """

    def __init__(self, frequency_field):
        self.frequency_field = frequency_field

    def __call__(self, value):
        frequency = value.get(self.frequency_field)
        if frequency > 7:
            raise ValidationError('Привычка должна выполняться НЕ реже 1 раза в неделю')
