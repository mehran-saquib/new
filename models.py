"""

This python file is for creating the columns in the database and other related models

"""

from sqlalchemy import Column, Float,  Integer, String
from database_ import Base

class variables(Base):
    __tablename__ = "variables"
    id = Column(Integer, primary_key=True, index=True)
    log_price=Column(Float)
    property_type=Column(String)
    room_type=Column(String)
    accommodates=Column(Integer)
    bathrooms=Column(Integer)
    bed_type=Column(String)
    cancellation_policy=Column(String)
    cleaning_fee=Column(String)
    city=Column(String)
    instant_bookable=Column(String) 
    bedrooms=Column(Integer)
    beds=Column(Integer)
