# from fastapi.testclient import TestClient
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker

# from src.database.database import Base, get_db
# from src.burger95s.main import app

# engine = create_engine("postgresql://postgres:210497@localhost/test", echo=True)

# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base.metadata.create_all(bind=engine)

# def override_get_db():
#     try:
#         db = TestingSessionLocal()
#         yield db
#     finally:
#         db.close()