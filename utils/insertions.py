from .models import *
from django.utils import timezone
from .random import unique_id


def insert_activity(ip, version, activity_id, user_id="anonymous"):
    

    che_act = Activity.objects.filter(activity_id=activity_id).first()
   
    if not che_act:

        Activity.objects.create(
            name=activity_id,
            activity_id=activity_id,
            platform="sfs",
            platform_name="app",
            status="approved",
            time = timezone.now()
        )
        
    TotalActivity.objects.create(
        ip=ip,
        user_id=user_id,
        activity_id=activity_id, 
        total_id = unique_id(),
        version=version,
        time = timezone.now()
        )
    
    print("executed")
    

        



def insert_error(ip, user_id, version, error_msg, activity):

    
    AllErrors.objects.create(
        ip=ip,
        error_id = unique_id(),
        error_msg = error_msg,
        user_id=user_id,
        activity = activity,
        version=version,
        status = "approved",
        time = timezone.now()
        )
        
    print("error inserted")



def create_activity(name, activity_id, platform, platform_name, status):
    Activity.objects.create(
        name=name,
        activity_id=activity_id,
        platform=platform,
        platform_name=platform_name,
        status=status,
        time = timezone.now()
    )