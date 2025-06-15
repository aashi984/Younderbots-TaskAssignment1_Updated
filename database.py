from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:@127.0.0.1:3306/vaccination_data"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Vaccination(Base):
    __tablename__ = "vaccinations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    age = Column(Integer, nullable=False)
    gender = Column(String(10), nullable=False)
    vaccine_name = Column(String(50), nullable=False)
    dose_number = Column(Integer, nullable=False)
    vaccination_date = Column(String(20), nullable=False)
    email = Column(String(100), nullable=False)
    contact_number = Column(String(20), nullable=False)


Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
