from rest_framework import serializers

from habits.models import Habit
from habits.validators import (RelatedHabitOrRewardValidator, TimeToCompleteLimitationValidator,
                               RelatedHabitValidation, PleasantHabitValidation, FrequencyValidation)


class HabitSerializer(serializers.ModelSerializer):

    class Meta:
        model = Habit
        fields = ('id', 'action', 'start', 'frequency', 'next_reminder_date', 'time_to_complete', 'place', 'user',
                  'related_habit', 'reward', 'is_public', 'is_pleasant')
        read_only_fields = ('user',)
        validators = [
            RelatedHabitOrRewardValidator('related_habit', 'reward'),
            TimeToCompleteLimitationValidator('time_to_complete'),
            RelatedHabitValidation('related_habit'),
            PleasantHabitValidation('related_habit', 'is_pleasant', 'reward'),
            FrequencyValidation('frequency')
        ]
