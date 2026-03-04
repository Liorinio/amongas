from typing import Optional, List
from sqlalchemy import String, ForeignKey, create_engine, Integer, Float, Column, DATETIME
from sqlalchemy.orm import declarative_base, Mapped, mapped_column , relationship, sessionmaker

engine = create_engine("example_string")
Base = declarative_base()

class Deployment(Base):
    __tablename__ = "deployments"
    id = Column(Integer, primary_key=True),
    db_name = Column(String)
    status = Column(String)
    username = Column(String)
    creation_time = Column(DATETIME)

Base.metadata.createall(engine)
Session = sessionmaker(bind=engine)
session = Session()