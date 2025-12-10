from django import forms
from .models import Workout

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['date', 'workout_type', 'duration_minutes', 'calories_burned', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
