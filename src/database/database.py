# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker


# SQLALCHEMY_DATABASE_URL = "postgresql:postgres:210497@localhost/burger95stest"

# engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True )

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

from contextlib import contextmanager
import warnings
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine("postgresql://postgres:210497@localhost/demo", echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
        
    except:
        # if we fail somehow rollback the connection
        warnings.warn("We somehow failed in a DB operation and auto-rollbacking...")
        db.rollback()
        raise

    finally:
        db.close()