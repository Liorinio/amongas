from sqlalchemy import Column, Integer, String, DATETIME, create_engine
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

engine = create_engine('postgresql://{}:{}@{}/{}'.format('postgres', 'postgres', 'postgres:5432', 'amongas_db'))

Base = declarative_base()

class Deployment(Base):
    __tablename__ = "deployments"
    id = Column(Integer, primary_key=True),
    db_name = Column(String, nullable=False)
    status = Column(String, nullable=False)
    username = Column(String, nullable=False)
    creation_time = Column(DATETIME(timezone=False))

Base.metadata.createall(engine)

