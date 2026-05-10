from sqlalchemy.orm import Session
from app.models.local_monitoring import LocalMonitoring



def get_locals(db:Session):
    return db.query(LocalMonitoring).all()


