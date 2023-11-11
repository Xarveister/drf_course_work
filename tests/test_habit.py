
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

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

    def test_create_habit(self):
        data = {
            'action': self.habit.action,
            'start': self.habit.start,
            'frequency': self.habit.frequency,
            'time_to_complete': self.habit.time_to_complete,
            'place': self.habit.place,
            'user': self.user
        }
        response = self.client.post(
            '/habit/create/',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertEqual(
            response.json(),
            {
                'id': (self.habit.id + 1),
                'action': 'test_action',
                'start': '2023-10-29T22:00:00Z',
                'frequency': 1,
                'next_reminder_date': None,
                'time_to_complete': '00:01:00',
                'place': 'test_place',
                'user': self.user.id,
                'related_habit': None,
                'reward': None,
                'is_public': False,
                'is_pleasant': False
            }
        )
        self.assertTrue(
            Habit.objects.all().exists()
        )

    def test_list_habit(self):
        response = self.client.get(
            '/habit/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json()['results'],
            [
                {'id': self.habit.id,
                 'action': 'test_action',
                 'start': '2023-10-29T22:00:00Z',
                 'frequency': 1,
                 'next_reminder_date': None,
                 'time_to_complete': '00:01:00',
                 'place': 'test_place',
                 'user': self.user.id,
                 'related_habit': None,
                 'reward': None,
                 'is_public': False,
                 'is_pleasant': False
                 }]
        )

    def test_retrieve_habit(self):
        response = self.client.get(
            f'/habit/{self.habit.id}/'
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {
                'id': self.habit.id,
                'action': 'test_action',
                'start': '2023-10-29T22:00:00Z',
                'frequency': 1,
                'next_reminder_date': None,
                'time_to_complete': '00:01:00',
                'place': 'test_place',
                'user': self.user.id,
                'related_habit': None,
                'reward': None,
                'is_public': False,
                'is_pleasant': False
            }
        )

    def test_update_habit(self):
        data = {
            'action': 'Test_updated_habit',
            'start': self.habit.start,
            'frequency': self.habit.frequency,
            'time_to_complete': self.habit.time_to_complete
        }
        response = self.client.patch(
            f'/habit/update/{self.habit.id}/',
            data=data
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            response.json(),
            {
                'id': self.habit.id,
                'action': 'Test_updated_habit',
                'start': '2023-10-29T22:00:00Z',
                'frequency': 1,
                'next_reminder_date': None,
                'time_to_complete': '00:01:00',
                'place': 'test_place',
                'user': self.user.id,
                'related_habit': None,
                'reward': None,
                'is_public': False,
                'is_pleasant': False
            }
        )

    def test_destroy_habit(self):
        response = self.client.delete(
            f'/habit/delete/{self.habit.id}/',
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
