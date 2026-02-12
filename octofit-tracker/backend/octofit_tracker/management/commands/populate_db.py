from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date, timedelta


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        self.stdout.write('Clearing existing data...')
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()
        User.objects.all().delete()

        # Create super hero users
        self.stdout.write('Creating users...')
        users_data = [
            {'username': 'ironman', 'email': 'tony.stark@marvel.com', 'first_name': 'Tony', 'last_name': 'Stark'},
            {'username': 'captainamerica', 'email': 'steve.rogers@marvel.com', 'first_name': 'Steve', 'last_name': 'Rogers'},
            {'username': 'blackwidow', 'email': 'natasha.romanoff@marvel.com', 'first_name': 'Natasha', 'last_name': 'Romanoff'},
            {'username': 'batman', 'email': 'bruce.wayne@dc.com', 'first_name': 'Bruce', 'last_name': 'Wayne'},
            {'username': 'superman', 'email': 'clark.kent@dc.com', 'first_name': 'Clark', 'last_name': 'Kent'},
            {'username': 'wonderwoman', 'email': 'diana.prince@dc.com', 'first_name': 'Diana', 'last_name': 'Prince'},
        ]

        users = []
        for user_data in users_data:
            user = User(**user_data)
            user.save()
            users.append(user)
        self.stdout.write(f'Created {len(users)} users')

        # Create teams - Team Marvel and Team DC
        self.stdout.write('Creating teams...')
        marvel_members = [str(users[0]._id), str(users[1]._id), str(users[2]._id)]
        dc_members = [str(users[3]._id), str(users[4]._id), str(users[5]._id)]

        team_marvel = Team(name='Team Marvel', members=marvel_members)
        team_marvel.save()

        team_dc = Team(name='Team DC', members=dc_members)
        team_dc.save()
        self.stdout.write('Created 2 teams: Team Marvel and Team DC')

        # Create workouts
        self.stdout.write('Creating workouts...')
        workouts_data = [
            {'name': 'Hero Cardio Blast', 'description': 'High-intensity cardio workout for super heroes', 'suggested_for': 'All heroes'},
            {'name': 'Super Strength Training', 'description': 'Strength training to build heroic muscles', 'suggested_for': 'Strength-focused heroes'},
            {'name': 'Agility Course', 'description': 'Speed and agility training for nimble heroes', 'suggested_for': 'Agility-focused heroes'},
        ]

        for workout_data in workouts_data:
            workout = Workout(**workout_data)
            workout.save()
        self.stdout.write(f'Created {len(workouts_data)} workouts')

        # Create activities for each user
        self.stdout.write('Creating activities...')
        activity_types = ['Running', 'Cycling', 'Strength Training', 'Flying', 'Combat Training']
        activity_count = 0
        for user in users:
            for i in range(3):
                activity = Activity(
                    user=str(user._id),
                    activity_type=activity_types[i % len(activity_types)],
                    duration=30 + (i * 15),
                    distance=5.0 + (i * 2.5),
                    calories=200 + (i * 100),
                    date=date.today() - timedelta(days=i)
                )
                activity.save()
                activity_count += 1
        self.stdout.write(f'Created {activity_count} activities')

        # Create leaderboard entries
        self.stdout.write('Creating leaderboard entries...')
        points_list = [150, 140, 130, 145, 155, 135]
        for i, user in enumerate(users):
            leaderboard = Leaderboard(
                user=str(user._id),
                points=points_list[i],
                week=7,
                year=2026
            )
            leaderboard.save()
        self.stdout.write(f'Created {len(users)} leaderboard entries')

        self.stdout.write(self.style.SUCCESS('Successfully populated the octofit_db database with test data!'))
