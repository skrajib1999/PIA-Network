from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from app.core.config import settings

engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()





from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# SQLAlchemy Database URL Format:
# postgresql://user:password@host:port/database
DATABASE_URL = settings.DATABASE_URL

# Engine setup
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,       # Check if connection is alive before using
    pool_size=10,             # Connection pool size
    max_overflow=20,          # Allow 20 extra connections beyond pool_size
    echo=False                # Set to True for SQL debug logs
)

# Session Local for dependency injection
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Declarative base class for models
Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
