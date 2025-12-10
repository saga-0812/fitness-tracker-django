
# Register your models here.
from django.contrib import admin
from .models import Workout

@admin.register(Workout)
class WorkoutAdmin(admin.ModelAdmin):
    list_display = ('date', 'workout_type', 'duration_minutes', 'calories_burned')
    list_filter = ('workout_type', 'date')

