from django.db import models

# Create your models here.

class Workout(models.Model):
    WORKOUT_TYPES = [
        ('walk', 'Walking'),
        ('run', 'Running'),
        ('gym', 'Gym'),
        ('cycle', 'Cycling'),
        ('yoga', 'Yoga'),
        ('other', 'Other'),
    ]

    date = models.DateField()
    workout_type = models.CharField(max_length=10, choices=WORKOUT_TYPES)
    duration_minutes = models.PositiveIntegerField()
    calories_burned = models.PositiveIntegerField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.get_workout_type_display()} on {self.date}"

