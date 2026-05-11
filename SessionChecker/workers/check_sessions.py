from app.services.surf_service import get_locals
from app.services.surf_service import get_users

from app.db.session import SessionLocal
from app.scrapers.main import screper

db = SessionLocal()

local_list = get_locals(db)
adress_list = get_users(db)



def check_locals(local_list, adress_list):
    for local in local_list:
        local_check = screper(local.name_local)

        if local_check:
            for adress in adress_list:
                if adress.local_monitoring_id  == local.id:
                    #send email

                    print()

check_locals(local_list, adress_list)