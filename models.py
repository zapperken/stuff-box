from datetime import datetime, timedelta
from sqlalchemy import Column, Integer, String, Text, Float, DateTime
from micro.database import Base

# database classes
class Entry(Base):
    __tablename__ = 'entries'
    id = Column(Integer, primary_key=True)
    title = Column(String(80))
    content = Column(Text())

class Track(Base):
    __tablename__ = 'tracks'
    id = Column
