

#this one is not completely done because I can not connect to MySQL server on '@R127.0.0.1'


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

  
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:biora_1234!R@127.0.0.1:3306/todoapp"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind= engine)

Base = declarative_base()