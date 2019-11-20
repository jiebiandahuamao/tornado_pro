from datetime import datetime
from sqlalchemy import Column,Integer,String,DateTime,Boolean
from connect import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True,autoincrement=True)
    username = Column(String(12))
    password = Column(String(20))
    creatime = Column(DateTime,default=datetime.now)
    _locked = Column(Boolean,default=False,nullable=False)


# Base.metadata.create_all()