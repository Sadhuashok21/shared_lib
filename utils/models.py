from django.db import models


class Activity(models.Model):
    name  = models.CharField(max_length=50)
    activity_id = models.CharField(max_length=50, unique=True)
    platform = models.CharField(max_length=10)
    platform_name = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    time = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'activity'


class TotalActivity(models.Model):
    ip = models.CharField(max_length=50)
    user_id = models.CharField(max_length=50)
    activity_id = models.CharField(max_length=50)
    total_id = models.CharField(max_length=50)
    platform = models.CharField(max_length=10, default="app")
    platform_name = models.CharField(max_length=50, default="sfs_blueprints")
    version = models.CharField(max_length=15)
    time = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'total_activity'


class AllErrors(models.Model):
    error_id = models.CharField(max_length=50)
    error_msg = models.TextField()
    user_id = models.CharField(max_length=40)
    ip = models.CharField(max_length=50)
    activity = models.TextField()
    platform = models.CharField(max_length=10, default="app")
    platform_name = models.CharField(max_length=50, default="sfs_blueprints")
    version = models.CharField(max_length=15)
    status = models.CharField(max_length=20)
    time = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'allerrors'




