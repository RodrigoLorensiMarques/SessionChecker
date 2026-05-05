from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.orm import relationship



from app.db.session import Base



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String(255), unique=True, nullable=False)

    local_monitoring = Column(Integer, ForeignKey("local_monitoring.id"), nullable=False)

    local_monitoring = relationship("LocalMonitoring")



