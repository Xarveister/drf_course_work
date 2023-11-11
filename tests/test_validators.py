from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from habits.models import Habit
from users.models import User


class ValidatorsTestCase(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            email='test@test.com',
            password='test',
            is_staff=True,
            is_superuser=True
        )
        self.client.force_authenticate(user=self.user)
        self.habit = Habit.objects.create(
            action='test_action',
            start='2023-10-29 22:00:00+00:00',
            frequency=1,
            time_to_complete='60',
            place='test_place',
            user=self.user
        )

    def test_RelatedHabitOrRewardValidator(self):
        data = {
            'action': 'test_action_val_1',
            'start': '2023-10-30 20:00:00+00:00',
            'frequency': 1,
            'time_to_complete': '60',
            'place': 'test_place_val_1',
            'user': self.user,
            'related_habit': self.habit.id,
            'reward': 'test_reward_val_1'
        }
        response = self.client.post(
            path='/habit/create/',
            data=data
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
        self.assertEquals(
            response.json(),
            {
                'non_field_errors':
                    ['Необходимо выбрать связанную привычку ИЛИ вознаграждение',
                     'Связанная привычка может быть ТОЛЬКО приятной']
            }
        )

    def test_TimeToCompleteLimitationValidator(self):
        data = {
            'action': 'test_action_val_2',
            'start': '2023-10-30 20:00:00+00:00',
            'frequency': 1,
            'time_to_complete': '160',
            'place': 'test_place_val_2',
            'user': self.user,
            'reward': 'test_reward_val_2'
        }
        response = self.client.post(
            path='/habit/create/',
            data=data
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
        self.assertEquals(
            response.json(),
            {'non_field_errors':
                ['Время выполнения привычки НЕ должно превышать 120 секунд']
             }
        )

    def test_RelatedHabitValidation(self):
        self.habit.is_pleasant = False
        self.habit.save()
        data = {
            'action': 'test_action_val_3',
            'start': '2023-10-30 20:00:00+00:00',
            'frequency': 1,
            'time_to_complete': '60',
            'place': 'test_place_val_3',
            'user': self.user,
            'related_habit': self.habit.id
        }
        response = self.client.post(
            path='/habit/create/',
            data=data
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
        self.assertEquals(
            response.json(),
            {
                'non_field_errors':
                    ['Связанная привычка может быть ТОЛЬКО приятной']
            }
        )

    def test_PleasantHabitValidation(self):
        data = {
            'action': 'test_action_val_4',
            'start': '2023-10-30 20:00:00+00:00',
            'frequency': 1,
            'time_to_complete': '60',
            'place': 'test_place_val_4',
            'user': self.user,
            'reward': 'test_reward_4',
            'is_pleasant': True
        }
        response = self.client.post(
            path='/habit/create/',
            data=data
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
        self.assertEquals(
            response.json(),
            {
                'non_field_errors':
                    ['Приятная привычка НЕ может иметь вознаграждения']
            }
        )

    def test_FrequencyValidation(self):
        data = {
            'action': 'test_action_val_5',
            'start': '2023-10-30 20:00:00+00:00',
            'frequency': 8,
            'time_to_complete': '60',
            'place': 'test_place_val_5',
            'user': self.user,
            'reward': 'test_reward_5',
        }
        response = self.client.post(
            path='/habit/create/',
            data=data
        )
        self.assertEquals(
            response.status_code,
            status.HTTP_400_BAD_REQUEST
        )
        self.assertEquals(
            response.json(),
            {
                'non_field_errors':
                    ['Привычка должна выполняться НЕ реже 1 раза в неделю']
            }
        )
