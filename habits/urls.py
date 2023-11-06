from django.urls import path
from habits.apps import HabitsConfig
from habits.views import HabitCreateAPIView, HabitListAPIView, PublicHabitsListAPIView, HabitRetrieveAPIView, \
    HabitUpdateAPIView, HabitDestroyAPIView

app_name = HabitsConfig.name

urlpatterns = [
    path('habit/create/', HabitCreateAPIView.as_view(), name='habit_create'),
    path('habit/', HabitListAPIView.as_view(), name='habit_list'),
    path('habit/public/', PublicHabitsListAPIView.as_view(), name='public_habit_list'),
    path('habit/<int:pk>/', HabitRetrieveAPIView.as_view(), name='habit_detail'),
    path('habit/update/<int:pk>/', HabitUpdateAPIView.as_view(), name='habit_update'),
    path('habit/delete/<int:pk>/', HabitDestroyAPIView.as_view(), name='habit_delete'),
]
