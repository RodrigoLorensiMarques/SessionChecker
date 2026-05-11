from sqlalchemy.orm import Session
from app.models.local_monitoring import LocalMonitoring
from app.models.user import User




def get_locals(db:Session):
    return db.query(LocalMonitoring).all()


def get_users(db:Session):
    return db.query(User).all()