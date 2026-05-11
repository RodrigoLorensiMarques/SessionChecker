from app.services.surf_service import get_locals
from app.services.surf_service import get_users
from app.services.notification_service import send_email

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
                    text_email = f"{local_check[2]}"
                    subject_email = f"Confira as novas sessões em {local_check[0]} no SurfMappers"

                    send_email(adress.email, text_email, subject_email)

check_locals(local_list, adress_list)