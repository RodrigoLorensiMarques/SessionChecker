from app.services.surf_service import get_locals
from app.db.session import SessionLocal
from app.scrapers.main import screper

db = SessionLocal()

local_list = get_locals(db)



def check_locals(local_list):
    for local in local_list:
        local_check = screper(local.name_local)

        if local_check:
            print ("Has session")
        

check_locals(local_list)