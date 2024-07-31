from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./users.db"
engine = create_engine(DATABASE_URL)
Sessionlocal = sessionmaker(autoflush=False,autocommit = False,bind=engine)
Base = declarative_base()

# DB="sqlite:///./students.db"
# engine1=create_engine(DB)
# Sessionlocal1= sessionmaker(autoflush=False,autocommit = False,bind=engine1)
# Base = declarative_base()