from sqlalchemy import Boolean, Column, Integer, String

from .db import Base


class URL(Base):
    __tablename__ = "storage"

    id = Column(Integer, primary_key=True)
    key = Column(String, unique=True, index=True)
    secret_key = Column(String, unique=True, index=True)
    aim_url = Column(String, index=True)
    status = Column(Boolean, default=True)
