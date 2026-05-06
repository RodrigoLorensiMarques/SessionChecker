from sqlalchemy import Column, Integer, String, ForeignKey

from app.db.session import Base



class LocalMonitoring(Base):
    __tablename__ = "local_monitoring"

    id = Column(Integer, primary_key=True, index=True)

    name_local = Column(String, nullable=False)





