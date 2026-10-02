from django.db import models


class Trains(models.Model):
    train_id = models.CharField(max_length=100, unique=True)
    train_number = models.CharField(max_length=20, unique=True)
    train_name = models.CharField(max_length=255)
    source_station = models.CharField(max_length=100)
    departure_time = models.TimeField()
    destination_station = models.CharField(max_length=100)
    arrival_time = models.TimeField()
    day = models.IntegerField(default=1)
    frequency = models.CharField(max_length=50, default='Daily')
    own = models.CharField(max_length=100)


    def __str__(self):
        return f"{self.train_name} ({self.train_id})"

    class Meta:
        db_table = 'trains'
        managed = True


class TrainSchedule(models.Model):
    DAYS = [
        ('MON', 'Monday'),
        ('TUE', 'Tuesday'),
        ('WED', 'Wednesday'),
        ('THU', 'Thursday'),
        ('FRI', 'Friday'),
        ('SAT', 'Saturday'),
        ('SUN', 'Sunday'),
        ('ALL', 'All Days'),
    ]
    train = models.ForeignKey(
        Trains,
        on_delete=models.CASCADE,
        related_name='schedules',
        db_column='train_id',
        to_field='train_id',
    )
    schedule = models.CharField(max_length=3, choices=DAYS)
    schedule_id = models.CharField(max_length=100, unique=True)
 
    def __str__(self):
        return f"{self.train.train_name} - {self.station} ({self.day_of_week})"

    class Meta:
        db_table = 'train_schedules'
        managed = True

class days(models.Model):
    train = models.ForeignKey(
            Trains,
            on_delete=models.CASCADE,
            related_name='days'
        )
    day_of_week = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.train.train_name} - {self.schedule}"

    class Meta:
        db_table = 'train_days'
        managed = True

class Stations(models.Model):
    station_id = models.CharField(max_length=50, unique=True)
    station_name = models.CharField(max_length=255)
    station_code = models.CharField(max_length=10, unique=True)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zone = models.CharField(max_length=100)
    division = models.CharField(max_length=100)
    station_category = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.station_name} ({self.station_code})"

    class Meta:
        db_table = 'stations'
        managed = True