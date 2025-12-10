# Create your views here.
from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Workout
from .forms import WorkoutForm

def home(request):
    # Show all workouts
    workouts = Workout.objects.order_by('-date', '-id')

    total_duration = workouts.aggregate(Sum('duration_minutes'))['duration_minutes__sum'] or 0
    total_calories = workouts.aggregate(Sum('calories_burned'))['calories_burned__sum'] or 0

    context = {
        'workouts': workouts,
        'total_duration': total_duration,
        'total_calories': total_calories,
    }
    return render(request, 'tracker/home.html', context)

def add_workout(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # name of url
    else:
        form = WorkoutForm()

    return render(request, 'tracker/add_workout.html', {'form': form})

