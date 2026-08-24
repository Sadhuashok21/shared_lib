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
    
    print("Executed: ", activity_id)
    
        


def insert_error(ip, user_id, version, error_msg, activity, error_code, platform, platform_name):
    
    AllErrors.objects.create(
        ip=ip,
        error_id = unique_id(),
        error_msg = error_msg,
        user_id=user_id,
        activity = activity,
        version=version,
        error_code = error_code,
        platform=platform,
        platform_name =platform_name,
        )
        
    print("Error inserted: ", error_msg)



def create_activity(name, activity_id, platform, platform_name, status):
    Activity.objects.create(
        name=name,
        activity_id=activity_id,
        platform=platform,
        platform_name=platform_name,
        status=status,
        time = timezone.now()
    )