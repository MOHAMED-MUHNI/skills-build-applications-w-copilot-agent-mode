import os
import sys
import django

# Setup Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'octofit_tracker.settings')
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
django.setup()

import random
from datetime import date, timedelta
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

# Create Users
def create_users():
    users = []
    for i in range(5):
        user = User(
            username=f'user{i}',
            email=f'user{i}@example.com',
            first_name=f'First{i}',
            last_name=f'Last{i}'
        )
        user.save()
        users.append(user)
    return users

# Create Teams
def create_teams(users):
    teams = []
    for i in range(2):
        member_ids = [str(users[j]._id) for j in range(i*2, min((i+1)*2, len(users)))]
        team = Team(name=f'Team{i}', members=member_ids)
        team.save()
        teams.append(team)
    return teams

# Create Workouts
def create_workouts():
    workouts = []
    for i in range(3):
        workout = Workout(
            name=f'Workout{i}',
            description=f'Description for workout {i}',
            suggested_for='All'
        )
        workout.save()
        workouts.append(workout)
    return workouts

# Create Activities
def create_activities(users):
    activities = []
    for user in users:
        for j in range(3):
            activity = Activity(
                user=str(user._id),
                activity_type=random.choice(['Running', 'Walking', 'Cycling']),
                duration=random.randint(20, 60),
                distance=random.uniform(1.0, 10.0),
                calories=random.uniform(100, 500),
                date=date.today() - timedelta(days=random.randint(0, 10))
            )
            activity.save()
            activities.append(activity)
    return activities

# Create Leaderboard
def create_leaderboard(users):
    for user in users:
        leaderboard = Leaderboard(
            user=str(user._id),
            points=random.randint(50, 200),
            week=7,
            year=2026
        )
        leaderboard.save()

def run():
    users = create_users()
    create_teams(users)
    create_workouts()
    create_activities(users)
    create_leaderboard(users)
    print('Random test data populated!')

if __name__ == '__main__':
    run()
