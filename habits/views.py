from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from habits.models import Habit
from habits.pagination import HabitsPagination
from habits.permissions import IsOwnerOrIsSuperuser
from habits.serializers import HabitSerializer


class HabitCreateAPIView(generics.CreateAPIView):
    """ Создание новой привычки """
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitListAPIView(generics.ListAPIView):
    """ Список всех привычек """
    serializer_class = HabitSerializer
    pagination_class = HabitsPagination
    permission_classes = [IsOwnerOrIsSuperuser]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Habit.objects.all()
        else:
            return Habit.objects.filter(user=self.request.user)


class PublicHabitsListAPIView(generics.ListAPIView):
    """ Список публичных привычек """
    serializer_class = HabitSerializer
    queryset = Habit.objects.filter(is_public=True)
    pagination_class = HabitsPagination
    permission_classes = [IsAuthenticated]


class HabitRetrieveAPIView(generics.RetrieveAPIView):
    """ Информация о привычке """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwnerOrIsSuperuser]


class HabitUpdateAPIView(generics.UpdateAPIView):
    """ Редактирование привычки """
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsOwnerOrIsSuperuser]


class HabitDestroyAPIView(generics.DestroyAPIView):
    """ Удаление привычки """
    queryset = Habit.objects.all()
    permission_classes = [IsOwnerOrIsSuperuser]
from django.shortcuts import render

# Create your views here.
