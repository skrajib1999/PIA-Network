from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import auth, user, mining, tasks
from app.core.config import settings
from app.models import models
from app.core.base import engine

# Create all DB tables (only use on dev, not in production with Alembic)
models.Base.metadata.create_all(bind=engine)

def create_application() -> FastAPI:
    app = FastAPI(
        title="PIA Network",
        description="Crypto mining simulation via Telegram & Web",
        version="1.0.0"
    )

    # Middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # You can restrict this for production
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Include routers
    app.include_router(auth.router)
    app.include_router(user.router)
    app.include_router(mining.router)
    app.include_router(tasks.router)

    return app

app = create_application()
