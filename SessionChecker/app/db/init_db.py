from app.db.session import engine, Base

from app.models.user import User
from app.models.local_monitoring import LocalMonitoring


def init_db():
    Base.metadata.create_all(bind=engine)