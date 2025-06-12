import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from app.api import auth, mining, user, tasks
from app.core.config import settings
from app.bot import start_bot

# Load .env
load_dotenv()

# Create FastAPI app
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.API_VERSION
)

# CORS for frontend/backend connection
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Routers ---
app.include_router(auth.router, prefix="/api/auth", tags=["Auth"])
app.include_router(user.router, prefix="/api/user", tags=["User"])
app.include_router(mining.router, prefix="/api/mining", tags=["Mining"])
app.include_router(tasks.router, prefix="/api/tasks", tags=["Tasks"])


# --- Root endpoint ---
@app.get("/")
def read_root():
    return {"message": "🚀 PIA Crypto Mining API Running!"}


# --- Bot + API startup ---
@app.on_event("startup")
async def startup_event():
    print("⚙️ Starting Telegram bot...")
    await start_bot()
    print("✅ Telegram bot started.")


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
