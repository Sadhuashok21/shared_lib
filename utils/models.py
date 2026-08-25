from django.db import models
from shared_lib.sfs_core.models import *




class TotalActivity(models.Model):
    ip = models.CharField(max_length=50)
    user = models.ForeignKey(
            AllUsers,
            null=True,
            blank=True,
            to_field="user_id",
            db_column="user_id",
            related_name="activity_user",
            on_delete=models.CASCADE,
        )
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
    error_code = models.IntegerField(default=200)
    user = models.ForeignKey(
            AllUsers,
            null=True,
            blank=True,
            to_field="user_id",
            db_column="user_id",
            related_name="error_user",
            on_delete=models.CASCADE,
        )
    ip = models.CharField(max_length=50)
    activity = models.TextField()
    platform = models.CharField(max_length=10, default="app")
    platform_name = models.CharField(max_length=50, default="sfs_blueprints")
    version = models.CharField(max_length=15)
    status = models.CharField(max_length=20, default='active')
    time = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'allerrors'



class DeviceFCM(models.Model):
    device = models.TextField()
    platform = models.CharField(max_length=10)
    platform_name = models.CharField(max_length=50)
    device_id = models.CharField(max_length=50)
    user = models.ForeignKey(
        AllUsers,
        null=True,
        blank=True,
        to_field="user_id",
        db_column="user_id",
        related_name="device_user",
        on_delete=models.CASCADE,
    )
    status = models.CharField(max_length=20,  default='active')
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'devices_fcm'

