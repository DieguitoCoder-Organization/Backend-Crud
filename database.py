from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import settings

# Obtiene la URL directamente desde el archivo config/env
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

# Configuración especial si se usa SSL con Supabase / Postgres remoto
engine_args = {}
if "supabase" in SQLALCHEMY_DATABASE_URL or "neon" in SQLALCHEMY_DATABASE_URL:
    engine_args["sslmode"] = "require"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()