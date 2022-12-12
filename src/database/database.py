import logging
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, scoped_session, sessionmaker


logger = logging.getLogger(__name__)

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:210497@localhost/demo"

Base = declarative_base()

class Database:
    def __init__(self, db_url: str = SQLALCHEMY_DATABASE_URL) -> None:
        self._engine = create_engine(db_url, echo=True)
        self._session_factory = scoped_session(
            sessionmaker(
                autocommit=False, 
                autoflush=False, 
                bind=self._engine
                )
        )

    def create_database(self) -> None:
        Base.metadata.create_all(self._engine)
    
    @contextmanager
    def session(self) -> Session:
        session: Session = self._session_factory()
        try:
            yield session

        except:
            logger.exception("Session rollback because of exception")
            session.rollback()
            raise

        finally:
            session.close()

