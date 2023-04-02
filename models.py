#the database table should contain one table with the fields first_name, last_name, phone_number
from db import Base
from sqlalchemy import TIMESTAMP, Column, Integer, String, false
from sqlalchemy.sql.expression import text


class Products(Base):
    __tablename__='products'
    id=Column(Integer, primary_key=True, nullable=False)
    product_name=Column(String, nullable=False )
    price=Column(String, nullable=False)
    rfid_tag=Column(String, nullable=False)
    timestamp=Column(TIMESTAMP(timezone=True), nullable=false, server_default=text('now()') )