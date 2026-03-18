
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql://hrms_7bi4_user:7ZE4aSIrulxU0EDlLvyYnXefsjih5vsp@dpg-d6p6d77afjfc739j1qqg-a.oregon-postgres.render.com/hrms_7bi4")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
