from pydantic import UUID4
from sqlalchemy import Column, String, DATETIME, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('postgresql://{}:{}@{}/{}'.format('postgres', 'postgres', 'postgres:5432', 'amongas_db'))
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

class Deployment(Base):
    __tablename__ = "deployments"
    id = Column(UUID4, primary_key=True),
    db_name = Column(String, nullable=False)
    status = Column(String, nullable=False)
    username = Column(String, nullable=False)
    creation_time = Column(DATETIME(timezone=False))

Base.metadata.createall(engine)

