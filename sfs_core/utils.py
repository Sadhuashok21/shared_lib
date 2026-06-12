from .models import *
from django.utils import timezone
from shared_lib.utils import random


def insert_dlv(ip, bp_id, type, user_id,download_type, version):


    bp = BP.objects.filter(bp_id=bp_id, status="approved").first()

    if bp:


        if type == "view":
            bp.fviews += 1
            bp.views += 1
        elif type == "like":
            bp.flikes += 1
            bp.likes += 1
        
        else:
            bp.fdownloads += 1
            bp.downloads += 1
            
        bp.save()

        BpDlv.objects.create(
            ip = ip,
            bp_pla_id = bp_id,
            type = type,
            user_id = user_id,
            download_type = download_type,
            dlv_id = random.unique_id(),
            platform="sfs",
            platform_name="app",
            version = version,
            time = timezone.now()
            )
    else:

        print("errror ")