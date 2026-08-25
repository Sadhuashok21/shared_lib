from .models import *
from django.utils import timezone
from .random import unique_id


def insert_activity(ip, version, activity_id, platform, platform_name, user_id=None):
    
        
    TotalActivity.objects.create(
        ip=ip,
        user_id=user_id,
        activity_id=activity_id, 
        total_id = unique_id(),
        version=version,
        platform_name=platform_name,
        platform=platform
        )
    
    print("Executed: ", activity_id)
    
        


def insert_error(ip, version, error_msg, activity, error_code, platform, platform_name, user_id=None):
    
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


